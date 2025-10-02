def soma_listas_mult(multlist):
    soma = 0
    for lista in multlist:
        soma += sum(lista)
    return soma

list1 = [2, 4, 6]
list2 = [1, 3, 5]
list3 = [3, 7, 11]
multlist = (list1, list2, list3)

print(soma_listas_mult(multlist))