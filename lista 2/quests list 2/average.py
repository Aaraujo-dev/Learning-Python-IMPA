def average(lista):
    soma = 0
    for item in lista:
        soma += item
        print(soma)
    media = soma / len(lista)
    return media

print("A ḿedia é:",average([1,2,3,4,5,6,7,8,9]))

