#Questão 5
'''
Nessa questão fiz o uso de list comprehension por curiosidade,
parecia ser uma forma mais simples de iterar já executando algo dentro da própria lista/vetor.
Em resumo, não foi simples, mas o resultado final ficou até que num formato bacana.
'''
class Vector3D:
    def __init__(self, vec):
        self.vec = vec

    def __add__(self, other):
        result = [self.vec[i] + other.vec[i] for i in range(len(self.vec))]
        return Vector3D(result)
    
    def __sub__(self, other):
        result = [self.vec[i] - other.vec[i] for i in range(len(self.vec))]
        return Vector3D(result)
    
    def __mul__(self, scalar):
        result = [elem * scalar for elem in self.vec]
        return Vector3D(result)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __str__(self):
        return str(self.vec)
