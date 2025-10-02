def std_deviation(lista):
    media = average(lista)
    subtr = minus_num(lista, media)
    quadrad = [x ** 2 for x in subtr]   
    media_quadrad = average(quadrad)
    desvio_padrao = media_quadrad ** 0.5   #como não pude importar bibliotecas, a forma de fazer a raiz quadrada foi essa
    
    return desvio_padrao