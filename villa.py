from tkinter import filedialog
from customtkinter import *
from PIL import Image, ImageTk, ImageEnhance
from tkinter import PhotoImage
import time
import tkinter as tk
#las villas deportivas, alojan a las selecciones
#varias selecciones pueden estar en la misma villa
#no se pueden alojar dos o mas selecciones que no tengan relaciones diplomaticas amistosas
#no es posible asignar una villa a una sola selección, a menos que sea estrictamente necesario
#la entrada de los datos es una matriz cuadrada (m) de 1 y 0 en archivo de texto plano, donde m[i][j] = 1 si las selecciones i y j no tienen relaciones diplomaticas amistosas, en otro caso m[i][j] = 0
#la salida de los datos es una matriz (s) de n x m (filas y columnas), n son las villas a construir y m las diferentes selecciones, donde s[i][j] = 1 si la selección i esta alojada en la villa j, en otro caso s[i][j] = 0

#lee el archivo de texto plano .txt
def ubicaciontxt():#filename ruta del archivo
    filename = filedialog.askopenfilename(
        filetypes=(
            ("Archivos de texto", "*.txt"),
        )
    ) 
    return filename

def vista(contenido,contenido_salida):#vista de la aplicacion
    ventana = CTk()
    ventana.title("Proyecto Final de ADA")
    ventana.configure(bg= "#051923")
    ventana.geometry("700x480")
    ventana.resizable(width=False, height=False)

    #Colores
    azulMuyClaro = "#91e5f6"
    azulOscuro = "#051923"
    azulMasOscuro = "#003554"
    azulClaro = "#006494"
    AzulMasClaro = "#0582ca"
    AzulVerdoso= "#00a6fb"

    #elementos dentro de la ventana
    imagenAbrir = Image.open("abrir.png")
    imagenMostrar = Image.open("mostrar.png")

    frame = CTkFrame(master=ventana, width=350, height=480, fg_color= azulMuyClaro)
    frame.pack_propagate(0)
    frame.pack(expand=True, side="right")

    mensajeBienvenida= CTkLabel(master=frame, text="¡Bienvenido!", 
                            text_color="#119da4", anchor="w", justify="left", font=("Segoe UI Black", 40)).pack(anchor="center", pady=(40, 30), padx=(10, 10))
    contenedor_pequeno= CTkFrame(master=frame, fg_color="#48cae4", border_color="#00b4d8", border_width=2)
    contenedor_pequeno.pack_propagate(3)
    contenedor_pequeno.pack(expand=True, fill="y", side= "top")

    MensajeInspirador=CTkLabel(master=contenedor_pequeno, 
                               text="Un pequeño país en Oriente Medio, un gran escenario \n para la gloria deportiva mundial."
                               ,text_color="#023e8a", anchor="w", justify="center", font=("Comic Sans MS", 12)).pack(anchor="center", 
                                                                                                                     padx=(5, 5))

    botonCargar= CTkButton(master=contenedor_pequeno, text="Cargar archivo y ejecutar", fg_color = AzulMasClaro, 
                           border_color=azulClaro, border_width=4, corner_radius=10, 
                           hover_color=AzulVerdoso, 
                           font=("Segoe UI Black", 16), text_color=azulClaro, 
                           width=350,command=lambda: main(contenedor_pequeno,contenido),
                           image=CTkImage(dark_image=imagenAbrir, light_image=imagenAbrir)).pack(anchor="center", 
                                                                                                 pady=(10, 10), 
                                                                                                 padx=(25, 25))
    

    ########################################################################
    #Función para los gifs
    def show_animated_gifs(gif_paths, size=(452, 480), opacity=0.5, switch_delay=5000, frame_delay=100):
        # Lista para almacenar los frames de cada GIF
        gifs = []
        for gif_path in gif_paths:
            frames = []
            gif_image = Image.open(gif_path)
            try:
                while True:
                    frame = gif_image.copy().resize(size, Image.BICUBIC)
                    # Convertir a 'RGBA' para manejar la opacidad
                    frame = frame.convert("RGBA")
                    # Modificar la opacidad
                    alpha = frame.split()[3]
                    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
                    frame.putalpha(alpha)
                    frames.append(ImageTk.PhotoImage(frame))
                    gif_image.seek(len(frames))  # Mover al siguiente frame
            except EOFError:
                gifs.append(frames)

        # Crear un label para mostrar los GIFs y hacer que el fondo sea negro
        label = tk.Label(ventana, bg='black', highlightthickness=0)
        label.pack(anchor='w')  # Alinear a la izquierda con un pequeño espacio

        current_gif_index = [0]
        current_frame_index = [0]

        # Función para actualizar el frame del GIF actual
        def update_frame():
            frames = gifs[current_gif_index[0]]
            frame = frames[current_frame_index[0]]
            label.configure(image=frame)
            current_frame_index[0] = (current_frame_index[0] + 1) % len(frames)
            ventana.after(frame_delay, update_frame)

        # Función para cambiar al siguiente GIF
        def switch_gif():
            current_gif_index[0] = (current_gif_index[0] + 1) % len(gif_paths)
            current_frame_index[0] = 0
            ventana.after(switch_delay, switch_gif)

        # Iniciar la animación del primer GIF
        ventana.after(0, update_frame)
        # Programar el cambio de GIFs
        ventana.after(switch_delay, switch_gif)

    # Llamar a la función con la lista de rutas de tus GIFs
    show_animated_gifs(
        ["baloncesto_pixel.gif", "futbol_pixel.gif", "beisbol_pixel.gif", "atletismo_pixel.gif", "villa_pixel_hermosa.gif"], 
        size=(460, 480), 
        opacity=0.5, 
        switch_delay=600, 
        frame_delay=100
    )
    #####################################
    ventana.mainloop()
    

def leer_matriz(filename):#lee la matriz del archivo de texto plano
    try:
        with open(filename, 'r') as archivo:
            contenido = archivo.read().strip()
        matriz = [list(map(int, fila.split())) for fila in contenido.split('\n')]
        return matriz,contenido
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


def main(contenedor_pequeno,contenido):#funcion principal
    try:
        print("Selecciona el archivo")
        archivo = ubicaciontxt()
        if not archivo:
            print("No se ha seleccionado ningún archivo.")
            return

        matriz,contenido = leer_matriz(archivo)
        if not matriz:
            print("La matriz no pudo ser leída o estaba vacía.")
            return

        n = contar_columnas(matriz)
        color, max_color = colorear_grafo(matriz)
        matriz_s = crear_matriz_s(color, max_color, n)
        escribir_matriz('salida.txt', matriz_s)
        contenido_salida = open('salida.txt', 'r').read()
        #print(contenido_salida)  # Para verificar el contenido de salida.txt
        
        # Cierra la ventana de la aplicación
        uwu=CTkLabel(master=contenedor_pequeno, 
                               text=contenido
                               ,text_color="#023e8a", anchor="w", justify="center", font=("Comic Sans MS", 12)).pack(anchor="center", 
                                                                                                                     padx=(5, 5), pady=(10, 10))
        maulopez = CTkLabel(master=contenedor_pequeno, 
                            text=contenido_salida
                            ,text_color="#023e8a", anchor="w", justify="center", font=("Comic Sans MS", 12)).pack(anchor="center", padx=(5, 5), pady=(16, 16))
        
        # Abre el archivo de salida en el programa predeterminado del sistema
        os.startfile('salida.txt')

    except Exception as e:
        print("")

vista("","")
    

