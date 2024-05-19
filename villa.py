#las villas deportivas, alojan a las selecciones
#varias selecciones pueden estar en la misma villa
#no se pueden alojar dos o mas selecciones que no tengan relaciones diplomaticas amistosas
#no es posible asignar una villa a una sola selección, a menos que sea estrictamente necesario
#la entrada de los datos es una matriz cuadrada (m) de 1 y 0 en archivo de texto plano, donde m[i][j] = 1 si las selecciones i y j no tienen relaciones diplomaticas amistosas, en otro caso m[i][j] = 0
#la salida de los daots es una matriz (s) de n x m (filas y columnas), n son las villas a construir y m las diferentes selecciones, donde s[i][j] = 1 si la selección i esta alojada en la villa j, en otro caso s[i][j] = 0

with open('entrada.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

with open('salida.txt', 'w') as archivo:
    archivo.write(contenido)

#idea: organizar primero los que se llevan bien para luego acomodar los que no se llevan bien
#nota: no se declara la cantidad de selecciones maximas por villa, podriamos tratar de ingresar de 3 a 2 selecciones por villa.