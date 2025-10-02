import turtle
import re

#QUESTÃO 1

def sortlists(lista1,lista2):
    one = 0  # percorre cada item da primeira lista 1 vez
    two = 0  # percorre cada item da segunda lista 1 vez
    result = []  # lista resultante
    #a complexidade será O(n+m) onde n e m são os respectivos tamanhos das listas
    while one < len(lista1) or two < len(lista2):
        if one < len(lista1) and (two >= len(lista2) or lista1[one] >= lista2[two]):
            result.append(lista1[one])
            one += 1
        elif two < len(lista2):
            result.append(lista2[two])
            two += 1
    return result

#QUESTÂO 2

def parentesiando(texto):
    contador = 0
    if '(' and ')' not in texto: #considerei que caso a entrada não possua pelo menos um '(' e ')' retorne falso
        return False
    for item in texto: # percorre cada item da entrada e soma 1 se for '(' e diminui 1 se for ')'
        if item == '(':
            contador += 1
        if item == ')':
            contador -= 1
        else:
            contador += 0
        if contador == -1: #caso haja um parentese ')' que não tenha '(' correspondente
            return False
    if contador == 0: # quando todos os parenteses estiverem bem definidos
        return True
    return False # quando há algum parentese '(' sem o seu ')'

#QUESTÂO 3
def compras(lista,n,k):
    memoria = []
    contador = 0  
    for item in lista:
        if item in memoria:
            pass
        else:
            if len(memoria) < k :   #nas primeiras iterações quando a memoria ainda não está completa
                memoria.append(item)
                contador += 1
            else: # quando a memoria já está cheia
                del memoria[0]
                memoria.append(item)
                contador += 1  
    return contador