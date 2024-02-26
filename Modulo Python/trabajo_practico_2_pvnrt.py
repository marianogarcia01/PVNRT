import numpy as np

#ejercicio 0

v1=np.full((3,1),1)
print('v1')
print(v1)
v2=np.arange(1,4).reshape(3,1)
print('v2')
print(v2)
A= np.array ([[-2,-4,2],[-2,1,2],[4,2,5]])
print('A')
print (A)

#ejercicio 1
#matrices de prueba
B=np.arange(1,10).reshape(3,3)
print('B')
print (B)
C= np.array([[0,2,3],[4,0,6],[7,0,0]])
print('C')
print (C)

#norma 0
def norma_0(array):
    
    '''
    (array) -> array #type contract
    Retorna un arreglo con la cantidad de elemntos diferentes a cero en cada fila a partir de una matriz
    >>> norma_0(np.array([[1,2,3],[4,5,6],[7,8,9]]))
    ([[3],
      [3],
      [3]])
    >>> norma_0(np.array([[0,2,3],[4,0,6],[7,0,0]]))
    ([[2],
      [2],
      [1]])
    '''
    norma0=[]
    forma= array.shape
    for i in range(0,forma[0]):
        contador= 0
        forma= array.shape
        for j in range(0,forma[1]):
            if array[i][j] != 0:
                contador=contador + 1
        norma0.append(contador)
    norma0_array=np.array(norma0)
    norma0_final=norma0_array.reshape(forma[0],1)
    return norma0_final

#norma infinito
def norma_infinito(array):
    '''
    (array) -> array #type contract
    Retorna una lista con el máximo valor de cada fila a partir de una matriz
    >>> norma_infinito(np.array([[1,2,3],[4,5,6],[7,8,9]]))
    ([[3],
      [6],
      [9]])
    >>> norma_infinito(np.array([[0,2,3],[4,0,6],[7,0,0]]))
    ([[3],
      [6],
      [7]])
    '''
    forma= array.shape
    norma_infinito_v2=np.max(array, axis=1)
    norma_infinito_v2=norma_infinito_v2.reshape(forma[0],1)
    return norma_infinito_v2

#norma 2
def norma_2(array):
    '''
    (array) -> array #type contract
    Retorna un arreglo con la raiz cuadrada de la suma de los elemntos de cada fila al cuadrado a partir de una matriz
    >>> norma_2(np.array([[1,2,3],[4,5,6],[7,8,9]]))
    ([[ 3.74],
      [ 8.77],
      [13.93]])
    >>> norma_2(np.array([[0,2,3],[4,0,6],[7,0,0]]))
    ([[3.61],
      [7.21],
      [7.  ]])
    '''    
    norma2=[]
    forma= array.shape
    suma=0
    for i in range(0,forma[0]):
        suma=0
        for j in range(0,forma[1]):
            suma= suma + array[i][j]**2
        raizcuadrada= suma**(1/2)
        norma2.append(raizcuadrada)
    redondeo_norma2=np.round(norma2,2)
    norma2_arreglo=np.array(redondeo_norma2)
    norma2_final=norma2_arreglo.reshape(forma[0],1)
    return norma2_final
            
#norma 1
def norma_1(array):
    '''
    (array) -> array #type contract
    Retorna un arreglo con la suma de los elemntos de cada fila de una matriz
    >>> norma_1(np.array([[1,2,3],[4,5,6],[7,8,9]]))
    ([[ 6],
      [15],
      [24]])
    >>> norma_1(np.array([[0,2,3],[4,0,6],[7,0,0]]))
    ([[ 5],
      [10],
      [ 7]])
    '''
    forma= array.shape
    norma1=np.sum(array, axis=1)
    norma_1=norma1.reshape(forma[0],1)
    return norma_1
        
#Ejercicio 2
#Dada una matriz en formato numpy array donde cada
#fila es un vector, obtener I2 de cada uno y ordenar
#de mayor a menor. Ordenar la matriz por filas según I2

def ordena_matriz(array):
    '''
    (array)->array
    Retorna una matriz donde sus filas estan ordenadas de mayor a menor según el I2 de cada una de las filas de la matriz original
    >>>ordena_matriz(np.array([[1,2,3],[4,5,6],[7,8,9]]))
    'norma I2 de cada vector'
    ([[ 3.74],
      [ 8.77],
      [13.93]])
    'norma I2 ordenada de mayor a menor'
    ([[ 13.93],
      [ 8.77],
      [3.74]])
    'matriz ordenada'
    [[7 8 9]
     [4 5 6]
     [1 2 3]]
     '''
    forma=array.shape
    vector_norma2=norma_2(array) #llama a la norma 2
    print(vector_norma2)
    vector_ordenado=np.sort(vector_norma2)[::-1] #ordena la norma de mayor a menor
    print(vector_ordenado)
    vector_indices = np.argsort(vector_norma2.reshape(1,forma[0])) #funcion que me da un vector con los indices del vector norma ordenado crecientemente
    print (vector_indices)
    vector_indices_inv = np.flip(vector_indices) #vector anterior ordenado de manera decreciente
    print (vector_indices_inv)
    matriz_ordenada = array[vector_indices_inv] #ordena la matriz segun el vector de indices invertido

    print('norma I2 de cada vector')
    print(vector_norma2)
    print('norma I2 ordenada de mayor a menor')
    print(vector_ordenado)
    print('matriz ordenada')
    return matriz_ordenada

#ejercicio 3
    
def media_desvio(array):
    '''
    (array)-> array
    Retorna una matriz donde a cada elemento de la matriz original se le resta la media y se lo divide por el desvio estandar, por columnas 
    media_desvio(np.array([[1,2,3],[4,5,6],[7,8,9]]))
    ([[-1.22474487, -1.22474487, -1.22474487],
      [ 0.        ,  0.        ,  0.        ],
      [ 1.22474487,  1.22474487,  1.22474487]])
    '''
    media=np.mean(array,axis=0)
    print(media)
    desvio_estandar=np.std(array, axis=0)
    print (desvio_estandar)
    matriz_media_desvio=(array-media)/desvio_estandar

    return matriz_media_desvio

        


    
