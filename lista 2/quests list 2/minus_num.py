def minus_num(lista, num):
    newlist = []
    for x in range(len(lista)):
        newlist.append(lista[x] - num)
    return newlist

resultado = minus_num([1, 3, 4, 5, 6], 3)
print(resultado)
