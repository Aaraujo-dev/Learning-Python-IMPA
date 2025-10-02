class List_Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linked_list:
    def __init__(self,head = None):
        self.head = head
        self.length = self.comprimento()
        
        
    def comprimento(self):
        no_atual = self.head
        comprimento = 0
        while no_atual:
            comprimento += 1
            no_atual = no_atual.next
        return comprimento
    
    def deletar_no(self, alvo):
        if not self.head:
            return        

        while self.head and self.head.val == alvo:
            self.head = self.head.next

        atual = self.head
        while atual and atual.next:
            if atual.next.val == alvo:
                atual.next = atual.next.next
            else:
                atual = atual.next

        self.comprimento = self.comprimento()

    def add(self, outra):
        if not self.head:
            return outra

        if not outra.head:
            return self
        
        atual = self.head
        while atual.next:
            atual = atual.next
    
        atual.next = outra.head
    
        nova_lista = Linked_list(self.head)
        nova_lista.comprimento = self.comprimento + outra.comprimento

        return nova_lista
