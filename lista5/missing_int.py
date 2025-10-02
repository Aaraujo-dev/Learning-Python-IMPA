def missing_int(listord):
    comeco, fim = 0, len(listord) - 1
    while comeco <= fim:
        meio = (comeco + fim) // 2
        print(comeco,meio,fim)
        if listord[meio] == meio + listord[0]:
            comeco = meio + 1
        else:
            fim = meio - 1
    
    return comeco + listord[0]

lista = [1,3,4,5,7]
print(missing_int(lista))