# Práctica 2: Merge Sort y Quick Sort
# Nombre: 
# Número de cuenta:

# ============== MERGE SORT ==============




def merge(left: list[int], right: list[int]) -> list[int]:
    """
    Fusiona dos listas ordenadas en una sola lista ordenada.
    
    Args:
        left: Lista ordenada izquierda
        right: Lista ordenada derecha
        
    Returns:
        Lista fusionada y ordenada
    """
    # TODO: Implementar
    pass
    #Definimos la lista que guarda la secuencia ordenada
    lista_ordenada = []
    i = j = 0
    #Mientras haya elementos en la lista izquierda y la derecha hacemos...
    while i < len(left) and j < len(right):
        #Si el elemento de la izuierda es menor o igual al de la derecha..
        if left[i] <= right[j]:
            lista_ordenada.append(left[i])
            i += 1 #Avanzamos el indice de la lista izquierda 
        else:
            lista_ordenada.append(right[j])
            j += 1 #Avanzamos el índice de la lista derecha 
    #Si quedan elementos en alguna de las listas, se añaden al final 
    lista_ordenada.extend(left[i:])
    lista_ordenada.extend(right[j:])

    print(f"Resultado de merge: {lista_ordenada}")
    return lista_ordenada


def merge_sort(arr: list[int]) -> list[int]:
    """
    Ordena una lista usando Merge Sort.
    
    Args:
        arr: Lista a ordenar
        
    Returns:
        Nueva lista ordenada
    """
    # TODO: Implementar
    pass
    #Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(arr) <= 1:
     return arr
    
    #Calculamos el punto medio de la lsita
    mitad = len(arr) // 2

    print(f"Dividiendo: {arr} -> {arr[:mitad]} | {arr[mitad:]}")
    #Para llamar recursivamente a merge_sort para dividir entre varias mitades hasta tener el caso baae
    left = merge_sort(arr[:mitad])
    right = merge_sort(arr[mitad:])

    return merge(left, right)

lista = [38, 27, 43, 3, 9, 82, 10]
print(f"Lista original: {lista}")
lista_ordenada = merge_sort(lista)
print(f"Lista ordenada: {lista_ordenada}")

# ============== QUICK SORT ==============

def partition(arr: list[int], low: int, high: int) -> int:
    """
    Particiona el arreglo usando el último elemento como pivote.
    
    Args:
        arr: Lista a particionar
        low: Índice inicial
        high: Índice final (pivote)
        
    Returns:
        Índice final del pivote
    """
    # TODO: Implementar
    pass
    pivote = arr[high]  # Elegimos el último elemento como pivote
    i = low - 1  # Índice del elemento más pequeño (Fuera del arreglo al principio)

    for j in range (low, high):
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivote:
            i += 1  # Incrementamos el índice del elemento más pequeño
            arr[i], arr[j] = arr[j], arr[i]  # Intercambiamos
    #Al final, debemos colocar el pivvote, en la posición correcta.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Colocamos el pivote en su posición correcta
    return i + 1  # Retornamos el índice del pivote

def quick_sort_inplace(arr: list[int], low: int = 0, high: int = None) -> None:
    """
    Ordena usando Quick Sort in-place.
    Modifica la lista original.
    
    Args:
        arr: Lista a ordenar
        low: Índice inicial
        high: Índice final
    """
    # TODO: Implementar
    pass
    #Caso inicial: Si given high is None, se asigna el valor del último índice de la lista
    if high is None:
        high = len(arr) - 1
    #Condición de parada: Si low es menor que high, se continúa con la partición y las llamadas recursivas
    if low < high:
        #Particionamos el arreglo
        pi = partition(arr, low, high)
        #Llamadas recursivas para las partes izquierda y derecha del pivote
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)



def quick_sort(arr: list[int]) -> list[int]:
    """
    Ordena usando Quick Sort (versión que retorna nueva lista).
    
    Args:
        arr: Lista a ordenar
        
    Returns:
        Nueva lista ordenada
    """
    # TODO: Implementar
    pass


    #Caso base: Si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[len(arr) // 2]  # Elegimos el pivote (elemento del medio)
        # Recursivamente ordenamos las partes izquierda y derecha del pivote
        left = quick_sort([x for x in arr if x < pivote])  # Elementos menores al pivote
        middle = [x for x in arr if x == pivote]  # Elementos iguales al pivote
        right = quick_sort([x for x in arr if x > pivote])  # Elementos mayores al pivote

        return quick_sort(left) + middle + quick_sort(right)  # Concatenamos las partes ordenadas
   
   
lista = [38, 27, 43, 3, 9, 82, 10]
print(f"Lista original: {lista}")
lista_ordenada2 = quick_sort(lista)
print(f"Lista ordenada: {lista_ordenada2}")

    # ============== QUICK SORT PIVOTE ALEATORIO ==============
import random
   
def quick_sort_random_pivot(arr: list[int]) -> list[int]:
        """
        Quick Sort con selección aleatoria de pivote.
        
        Args:
        arr: Lista a ordenar
        
        Returns:
        Nueva lista ordenada
        """
    # TODO: Implementar
        pass
        if len(arr) <= 1:
            return arr
        else:
            pivote = random.choice(arr)  # Elegimos un pivote aleatorio
            left = quick_sort_random_pivot([x for x in arr if x < pivote])  # Elementos menores al pivote
            middle = [x for x in arr if x == pivote]  # Elementos iguales al pivote
            right = quick_sort_random_pivot([x for x in arr if x > pivote])  # Elementos mayores al pivote
            return quick_sort_random_pivot(left) + middle + quick_sort_random_pivot(right)  # Concatenamos las partes ordenadas
        
        
lista = [38, 27, 43, 3, 9, 82, 10]
print(f"Lista original: {lista}")
lista_ordenada3 = quick_sort_random_pivot(lista)
print(f"Lista ordenada: {lista_ordenada3}") 