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