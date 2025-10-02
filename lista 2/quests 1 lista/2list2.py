def sum_cumulative(lista):
    nova_lista = []
    soma = 0
    for item in lista:
        soma += item
        nova_lista.append(soma)
    return nova_lista

