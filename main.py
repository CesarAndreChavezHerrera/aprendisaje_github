#test de git con archivo generico de python


print("bienvenido a la calculadora ")
print("ingrese la operacion que quiere realizar")
print("[1]suma, [2]resta,[3]multiplicacion, [4]divicion")
opcion = input()

print("ingrese el primer valor ")
numero_uno = input()

print("ingrese el segundo valor")
numero_dos = input()


 

def suma(a , b ):
    r = int(a) +int(b)
    print("rel resultado es de:")
    print(r)
    pass

if opcion == "1":
    suma(numero_uno,numero_dos)