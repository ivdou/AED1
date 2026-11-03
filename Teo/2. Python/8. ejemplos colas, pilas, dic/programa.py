def sumar(a, b):
    if(a%2==0):
        print(str(a) + " es un numero par")
    if(a==b):
        print(str(a) + " y " + str(b) + " son iguales")
    
    return a + b

def restar(a, b):
    return a - b

arg1:int = 6
arg2:int = 4
res1:int = sumar(arg1,arg2)
res2:int = restar(res1,1)
print(res2)
