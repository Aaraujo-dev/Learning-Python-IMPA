def isAnagram(pal1, pal2):
    pal1 = pal1.lower()
    pal2 = pal2.lower()   
    if sorted(pal1) == sorted(pal2):
        return True
    else:
        return False
print(isAnagram("loGa", "galo"))
