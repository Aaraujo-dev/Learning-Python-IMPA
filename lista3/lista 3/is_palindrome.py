def is_palindrome (palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False
    
print(is_palindrome("lomolb"))