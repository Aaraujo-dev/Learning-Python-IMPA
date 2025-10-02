list = [1,2,3,5,4,5]
mytuple = tuple(list)

mydict = {
"doroteira": list,
'a' : 2,
2: 'u',
"sus": mytuple
}


x = (mydict.keys())
print(x)
print(mydict.values())
print(mydict.items())

myset = {1,2,3,'oi',("farinha","parauapebas-P","2")}
print(myset)
print(mydict.get("doroteia"))