def int_to_roman(num):
    # Tabela de valores romanos
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

# Testando a função
print(int_to_roman(1))    # Saída: I
print(int_to_roman(58))   # Saída: LVIII
print(int_to_roman(1994)) # Saída: MCMXCIV
print(int_to_roman(3999)) # Saída: MMMCMXCIX