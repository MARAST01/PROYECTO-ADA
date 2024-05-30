#las villas deportivas, alojan a las selecciones
#varias selecciones pueden estar en la misma villa
#no se pueden alojar dos o mas selecciones que no tengan relaciones diplomaticas amistosas
#no es posible asignar una villa a una sola selección, a menos que sea estrictamente necesario
#la entrada de los datos es una matriz cuadrada (m) de 1 y 0 en archivo de texto plano, donde m[i][j] = 1 si las selecciones i y j no tienen relaciones diplomaticas amistosas, en otro caso m[i][j] = 0
#la salida de los datos es una matriz (s) de n x m (filas y columnas), n son las villas a construir y m las diferentes selecciones, donde s[i][j] = 1 si la selección i esta alojada en la villa j, en otro caso s[i][j] = 0

#lee el archivo de texto plano .txt
def leer_matriz(filename):
    with open(filename, 'r') as archivo:
        contenido = archivo.read().strip()
    matriz = [list(map(int, fila.split())) for fila in contenido.split('\n')]
    return matriz

def contar_columnas(matriz):
    if matriz:
        return len(matriz[0])
    return 0

def colorear_grafo(matriz):
    n = len(matriz)
    color = [-1] * n
    color[0] = 0
    disponible = [True] * n
    
    for u in range(1, n):
        for i in range(n):
            if matriz[u][i] == 1 and color[i] != -1:
                disponible[color[i]] = False
        
        cr = 0
        while cr < n:
            if disponible[cr]:
                break
            cr += 1
        
        color[u] = cr
        disponible = [True] * n
    
    max_color = max(color) + 1
    return color, max_color

def crear_matriz_s(color, max_color, n):
    s = [[0] * n for _ in range(max_color)]
    for i in range(n):
        s[color[i]][i] = 1
    return s

def escribir_matriz(filename, matriz):
    with open(filename, 'w') as archivo:
        for fila in matriz:
            archivo.write(' '.join(map(str, fila)) + '\n')

def main():
    matriz = leer_matriz('entrada.txt')
    n = contar_columnas(matriz)
    
    color, max_color = colorear_grafo(matriz)
    matriz_s = crear_matriz_s(color, max_color, n)
    
    escribir_matriz('salida.txt', matriz_s)

main()

#nota: no se declara la cantidad de selecciones maximas por villa, podriamos tratar de ingresar de 3 a 2 selecciones por villa
#idea de resolverlo con arboles binarios de busqueda, donde el nodo h-1 sea la villa y los nodos h sean las selecciones
#con respecto a lo anterior entonces cada nodo h-2 para atras define quien puede estar en la misma villa