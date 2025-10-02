#Questão 1
'''
Letra A:
1
3
Letra B:
Value is bad

Letra C:
que massa

Letra D:
[1,2,5,4]
'''
#Questão 2
'''
Letra A - O erro está no médoto "__ints__" que atrapalhou a inicialização da função
basta mudar essa parte para "__init__" e o erro irá desaparecer.

Letra B - A saída padrão será:
[]
[2.0 ,1.0]

Letra C - Não está de acordo, a saída é uma soma de 2 vetores iguais
e não a soma de 2 vetores diferentes como deveria acontecer.
Na linha 10 em:
new_vector[i] = self.values[i] + self.values[i]
deveria haver a soma de self.values[i] e other_vector.values[i]
'''
#Questão 3 Letra A
class Circle:
    def __init__(self, orig, raio):
        self.orig = orig
        self.raio = raio

    def localiza_ponto(self, ponto):
        dist_pontos = ((self.orig[0] - ponto[0])**2 + (self.orig[1] - ponto[1])**2)**0.5
        if dist_pontos < self.raio:
            return "dentro"
        elif dist_pontos == self.raio:
            return "sobre"
        else:
            return "fora"
#Questão 3 Letra B
class Line_Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def ponto_sobre(self, ponto):
        x1, y1 = self.point1
        x2, y2 = self.point2
        x, y = ponto
        
        if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
            return True
        else:
            return False
#Questão 4
def analise_circuloreta(circulo, reta):
    if (circulo.localiza_ponto(reta.point1) == "dentro" and 
        circulo.localiza_ponto(reta.point2) == "dentro"):
        return True
    else:
        return False
    
'''
Um exemplo de como usar isso é:
circle = Circle((0, 0), 5.0)
reta = Line_Segment((1, 1), (0, 4))
print(analise_circuloreta(circle, reta))
'''