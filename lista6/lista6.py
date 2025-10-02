# QUestão 1
def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Questão 2
#Letra A
def pascalnline(n):
    pascal = []
    for i in range(1,n+1):
        if i == 1:
            pascal.append([1])
        else:
            linha_atual = []
            for j in range(i):
                if j == 0 or j == i-1:
                    linha_atual.append(1)
                else:
                    x = pascal[i-2][j-1] + pascal[i-2][j]
                    linha_atual.append(x)
            pascal.append(linha_atual)
    return pascal

#Letra B
'''
A complexidade no pior caso é O(n^2) por ter 2 loops um dentro do outro,
e conforme n aumenta ambos tem um aumento no número de operações que acaba sendo
exponencial
'''

#Quetsão 3
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

        # remove nós correspondentes ao alvo
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

        #o último nó da lista self
        current = self.head
        while current.next:
            current = current.next
        current.next = other.head

        #cria a nova lista encadeada se self não estiver vazio
        new_list_head = self.head if self.head else other.head
        new_list = Linked_list(new_list_head)

        #muda comprimento na nova lista
        new_list.tam = self.tam + other.tam

        return new_list
'''
De modo geral os códigos são basicamente atribuições  e comparações de valores, 
a complexidade acaba sendo constante por causa do número de operações não ter aumento linear ou exponencial
'''
    
#Questão 4
'''
Infelizmente não consegui terminar essa a tempo,
preferi resolver alguns erros específicos na questão 5
pois ainda faltava muita coisa nessa e achei que resolver
a próxima seria o mais promissor dado o tempo.

Basicamente estava tentando fazer um for que analisava termo a termo
e ia adicionando esses termos numa variável que seriam os coeficientes,
o for ia adicionando esses coeficientes até chegar ao x, depois avaliaria o termo seguinte ao x,
se fosse um '^' continuava adicionando em outra variavel que seria o expoente.
E iria seguindo nisso até ter algum tipo de processamento específico para o x e o coeficiente de grau 0.
Só que percebi que teriam vários casos específicos que iriam acabar fazendo o código ficar muito grande,
aí tive de deixar como está.
'''
def polystring(poly):
    
    for indice,item in enumerate(poly):
        dicionario = {}
        chave = ''
        valor = ''
        y += indice
        if item == 'x':
            if poly[y+1] == '^':
                while poly[y+2] != '+' or '-' and y != len(poly)  :
                    chave = chave + poly[y+2]
                    y +=1
            while y-1 != -1 and poly[y-1] != '+' or '-' :
                valor = poly[y-1] + valor
                y += -1
    indice += 1    
    dicionario[chave] = valor    


#Questão 5
# Fiz o código considerando o dicionário tendo tanto 
# os valores quanto as chaves tendo números no formato int
def polinomiza(dicionario):
    mystrng = ''
    chaves = list(dicionario.keys())
    for x,i in enumerate(chaves):
        print(i , x)
        if i == 0: #constante
            if dicionario[i] > 0:
                mystrng += '+'
            mystrng += str(dicionario[i])
        elif i == 1: #exponencial 1, apenas variável x
            if x == 0:
                if dicionario[i] < 0:
                    mystrng += '-'
            else:
                if dicionario[i] > 0:
                    mystrng += '+'
            if dicionario[i] == 1:
                mystrng += 'x'
            if dicionario[i] == -1:
                mystrng += '-x'
            else:
                mystrng += str(dicionario[i]) + 'x'
        else:      #expoentes > 1 do polinomio
            if x == 0:
                if dicionario[i] > 0:
                    mystrng += ''
            else:
                if dicionario[i] > 0:
                    mystrng += '+'
            if dicionario[i] == 1:
                mystrng += 'x^'
            elif dicionario[i] == -1:
                mystrng += '-x^'
            else:
                mystrng += str(dicionario[i]) + 'x^'
            mystrng += str(i)
    return mystrng