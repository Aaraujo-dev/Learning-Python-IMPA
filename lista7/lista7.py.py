import matplotlib.pyplot as plt
import pandas as pd
import csv

#Questão 1
def cria_arquivo_csv():
    x = -3/2
    with open('sla2.csv','w',newline='') as csvfile:
        head = ['x','y']
        escritor = csv.DictWriter(csvfile, fieldnames = head)
        escritor.writeheader()
        
        for z in range(1,1001):
            y = x**8 - 3*x**4 + 2*x**3 - 2*x**2 -x + 2
            escritor.writerow({'x':x,'y':y})
            x += 3/999

def plota():
    df = pd.read_csv('sla2.csv')
    x = df['x']
    y = df['y']

    plt.plot(x, y, color='blue', linestyle='solid')
    plt.title('x⁸-3x⁴+2x³-2x²-x + 2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

'''
Deixei as 2 funções separadas para facilitar a execução do código,
basta apenas executá-las uma por vez, a primeira cria um arquivo contendo
os valores dos 1000 pontos da função no intervalo dado, a segunda printa esses 
pontos e seus valores respectivos.
'''

#Questão 2
def merge_intervals(lista):
    n = len(lista)
    for i in range(n - 1):#Retorna a lista só que com os intervalos em ordem com base no 1 termo.
        indicemin = i
        for j in range(i + 1, n):
            if lista[j][0] < lista[indicemin][0]:
                indicemin = j
        lista[i], lista[indicemin] = lista[indicemin], lista[i]
    listatual = []
    listatual.append(lista[0])
    lista.pop(0) # Adicionei o primeiro intervalo em uma outra lista e o removi da primeira
    for interv in lista:
        if interv[0] <= listatual[-1][1]: #funde intervalos contidos ou com ao menos 1 termo sobre o outro
            listatual[-1][1] = max(interv[1],listatual[-1][1]) #maior termo permanece 
        else:
            listatual.append(interv)
    return listatual

#Questão 3
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

#Questão 4
'''
Apenas peguei a função que usei na lista 6,
implementei na classe a função para palíndromo,
usando uma manipulação de lista consideravelmente
simples.
'''
class List_Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linked_list:
    def __init__(self, head=None):
        self.head = head
        self.tam = self.tamanho()

    def tamanho(self):
        current = self.head
        tam = 0
        while current:
            tam += 1
            current = current.next
        return tam

    def delete_node(self, target):
        if not self.head:
            return

        while self.head and self.head.val == target:
            self.head = self.head.next

        current = self.head
        while current and current.next:
            if current.next.val == target:
                current.next = current.next.next
            else:
                current = current.next

        self.tam = self.tamanho()

    def __add__(self, other):
        if not self.head:
            return other
        if not other.head:
            return self

        current = self.head
        while current.next:
            current = current.next
        current.next = other.head

        new_list_head = self.head if self.head else other.head
        new_list = Linked_list(new_list_head)

        new_list.tam = self.tam + other.tam

        return new_list
    
    def is_palindrome(self):
        vals = []
        current = self.head
        while current:
            vals.append(current.val)
            current = current.next
        return vals == vals[::-1]
    
#Questão 5

