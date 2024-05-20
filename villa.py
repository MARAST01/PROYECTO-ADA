#las villas deportivas, alojan a las selecciones
#varias selecciones pueden estar en la misma villa
#no se pueden alojar dos o mas selecciones que no tengan relaciones diplomaticas amistosas
#no es posible asignar una villa a una sola selección, a menos que sea estrictamente necesario
#la entrada de los datos es una matriz cuadrada (m) de 1 y 0 en archivo de texto plano, donde m[i][j] = 1 si las selecciones i y j no tienen relaciones diplomaticas amistosas, en otro caso m[i][j] = 0
#la salida de los datos es una matriz (s) de n x m (filas y columnas), n son las villas a construir y m las diferentes selecciones, donde s[i][j] = 1 si la selección i esta alojada en la villa j, en otro caso s[i][j] = 0

#lee el archivo de texto plano .txt
with open('entrada.txt', 'r') as archivo:
    contenido = archivo.read()
    #print(contenido)

#funcion que cuenta las columnas (cantidad de selecciones)
def contar_columnas(matriz_texto):
    filas = matriz_texto.strip().split('\n')
    if filas:
        primera_fila = filas[0].split()
        numero_de_columnas = len(primera_fila)
        return numero_de_columnas
    else:
        return 0
matriz_texto = contenido
print(contar_columnas(matriz_texto))


#escribe la nueva matriz de salida n x m en un archivo de texto plano .txt
with open('salida.txt', 'w') as archivo:
    archivo.write(contenido)

#nota: no se declara la cantidad de selecciones maximas por villa, podriamos tratar de ingresar de 3 a 2 selecciones por villa
#idea de resolverlo con arboles binarios de busqueda, donde el nodo h-1 sea la villa y los nodos h sean las selecciones
#con respecto a lo anterior entonces cada nodo h-2 para atras define quien puede estar en la misma villa