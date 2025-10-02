def is_palindrome (palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False
    
print(is_palindrome("lomolb"))

def get_vogals(palavra):
    vogais = "aeiou"
    get = []
    for vogal in vogais:
        for letter in palavra:
            if vogal == letter and vogal not in get:
                get += vogal
    return "[" + ",".join(get) + "]"

x = get_vogals("uoiea")
print(x)

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

y = enconder("B batata")
print(y)


def isAnagram(pal1, pal2):
    pal1 = pal1.lower()
    pal2 = pal2.lower()   
    if sorted(pal1) == sorted(pal2):
        return True
    else:
        return False
print(isAnagram("loGa", "galo"))
