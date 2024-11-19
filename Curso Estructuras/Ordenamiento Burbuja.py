#Ordenamiento de burbuja

list = [4, 2, 6, 8, 5, 7]

print(list)
for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            aux = list[j]
            list[j] = list[j+1]
            list[j+1] = aux
            print(list)

list = [70, 90, 0, 80, 60, 85]

def bubbleSort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if list[j] > list[j+1]:
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
    return lista

print(f"Lista antes del ordenamiento: {list}")
print(f"Lista después del ordenamiento: {bubbleSort(list)}")