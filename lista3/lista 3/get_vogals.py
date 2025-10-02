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
