def enconder(frase):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    newpal = ""
    for elem in frase:
        if elem in alfabeto:
            new_index = (alfabeto.index(elem) - 1) % 26
            newpal += alfabeto[new_index]
        else:
            newpal += elem
    return newpal

y = esconder("B batata")
print(y)
