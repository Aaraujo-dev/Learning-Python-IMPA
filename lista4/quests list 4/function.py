def analise_circuloreta(circulo, reta):
    if (circulo.localiza_ponto(reta.point1) == "dentro" and 
        circulo.localiza_ponto(reta.point2) == "dentro"):
        return True
    else:
        return False