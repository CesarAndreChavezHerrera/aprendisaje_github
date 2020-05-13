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

def resta(a , b):

    r = int(a) - int(b)
    print("el resultado es de:")
    print (r)

def multiplicacion(a,b):

    r = int(a) * int(b)
    print("el resultado es de ")
    print(r)


def dividir(a,b):
    r = int(a) / int(b)
    
    print("el resultado es de")
    
    print(r)


if opcion == "1":
    suma(numero_uno,numero_dos)

elif opcion == "2":

    resta(numero_uno,numero_dos)

elif opcion == "3":

    multiplicacion(numero_uno,numero_dos)
    
elif opcion == "4":

    dividir(numero_uno,numero_dos)
    
else:
    print("opcion no valida ")
    pass