def two_sum(nums, target):
    for i in range(len(nums)):
        x = 0
        while x < len(nums):
            if target - nums[x] == nums[i]:
                return [x, i] #printa os indices não os numeros em si
            x += 1

def average(lista):
    soma = 0
    for item in lista:
        soma += item
    media = soma / len(lista)
    return media

def minus_num(lista, num):
    newlist = []
    for x in range(len(lista)):
        newlist.append(lista[x] - num)
    return newlist

def std_deviation(lista):
    media = average(lista)
    subtr = minus_num(lista, media)
    quadrad = [x ** 2 for x in subtr]   
    media_quadrad = average(quadrad)
    desvio_padrao = media_quadrad ** 0.5   #como não pude importar bibliotecas, a forma de fazer a raiz quadrada foi essa
    
    return desvio_padrao