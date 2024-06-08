from tkinter import filedialog
from customtkinter import *
#las villas deportivas, alojan a las selecciones
#varias selecciones pueden estar en la misma villa
#no se pueden alojar dos o mas selecciones que no tengan relaciones diplomaticas amistosas
#no es posible asignar una villa a una sola selección, a menos que sea estrictamente necesario
#la entrada de los datos es una matriz cuadrada (m) de 1 y 0 en archivo de texto plano, donde m[i][j] = 1 si las selecciones i y j no tienen relaciones diplomaticas amistosas, en otro caso m[i][j] = 0
#la salida de los datos es una matriz (s) de n x m (filas y columnas), n son las villas a construir y m las diferentes selecciones, donde s[i][j] = 1 si la selección i esta alojada en la villa j, en otro caso s[i][j] = 0

#lee el archivo de texto plano .txt
def ubicaciontxt():#acceder al archivo de texto plano
    filename = filedialog.askopenfilename(
        filetypes=(
            ("Archivos de texto", "*.txt"),
        )
    ) 
    return filename

def vista():#vista de la aplicacion
    app = CTk()
    app.geometry("500x500")
    btn = CTkButton(master=app, text="Seleccionar archivo", command=lambda: main(app))
    btn.place(relx=0.5, rely=0.5, anchor="center")
    app.mainloop()
    

def leer_matriz(filename):#lee la matriz del archivo de texto plano
    try:
        with open(filename, 'r') as archivo:
            contenido = archivo.read().strip()
        matriz = [list(map(int, fila.split())) for fila in contenido.split('\n')]
        return matriz
    except Exception as e:
        print(f"Error al leer la matriz desde el archivo: {e}")
        return []

def contar_columnas(matriz):#cuenta las columnas de la matriz
    if matriz:
        return len(matriz[0])
    return 0

def colorear_grafo(matriz):#colorea el grafo
    n = len(matriz)
    color = [-1] * n # Inicializa el color de cada selección a -1 (sin color)
    color[0] = 0  #Asigna el primer color (0) a la primera selección
    disponible = [True] * n # Inicializa todos los colores como disponibles
    #u representa el índice de la selección actual
    #i representa el índice de la selección en el bucle interior for dentro del bucle que controla u.

    for u in range(1, n):
        # Marca los colores que no están disponibles debido a selecciones adyacentes ya coloreadas
        for i in range(n):
            if matriz[u][i] == 1 and color[i] != -1:
                disponible[color[i]] = False
        # Encuentra el primer color disponible
        cr = 0
        while cr < n: #Este bucle while encuentra el primer color disponible (disponible[cr] == True).
            if disponible[cr]:#Cuando encuentra un color disponible, lo asigna a la selección u (color[u] = cr).
                break
            cr += 1 
        # Asigna el primer color disponible a la selección u
        color[u] = cr
        
        # Restaura la disponibilidad de los colores para la próxima iteración
        disponible = [True] * n #Restaura la disponibilidad de todos los colores para la siguiente iteración. Esto asegura que cada selección pueda ser evaluada con todos los colores disponibles nuevamente.
    # Determina el número máximo de colores utilizados
    max_color = max(color) + 1 #max_color calcula el número máximo de colores utilizados sumándole 1 al valor máximo en la lista color (ya que los colores comienzan en 0).
    return color, max_color

def crear_matriz_s(color, max_color, n):#crea la matriz s
    s = [[0] * n for _ in range(max_color)]
    for i in range(n):
        s[color[i]][i] = 1
    return s

def escribir_matriz(filename, matriz):#escribe la matriz en el archivo de texto plano
    with open(filename, 'w') as archivo:
        for fila in matriz:
            archivo.write(' '.join(map(str, fila)) + '\n')


def main(app):#funcion principal
    print("Selecciona el archivo")
    archivo = ubicaciontxt()
    if not archivo:
        print("No se ha seleccionado ningún archivo.")
        return

    matriz = leer_matriz(archivo)
    if not matriz:
        print("La matriz no pudo ser leída o estaba vacía.")
        return

    n = contar_columnas(matriz)
    color, max_color = colorear_grafo(matriz)
    matriz_s = crear_matriz_s(color, max_color, n)
    escribir_matriz('salida.txt', matriz_s)
    contenido_salida = open('salida.txt', 'r').read()
    print(contenido_salida)  # Para verificar el contenido de salida.txt

    # Cierra la ventana de la aplicación
    app.destroy()

    # Abre el archivo de salida en el programa predeterminado del sistema
    os.startfile('salida.txt')
    
vista()