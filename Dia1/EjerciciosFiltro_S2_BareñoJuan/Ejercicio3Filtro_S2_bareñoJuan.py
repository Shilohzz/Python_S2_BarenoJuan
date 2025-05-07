def sumar(a,b):
    print(a+b)

def restar(a,b):
    print(a-b)

def dividir(a,b):
    print(a/b)

def multiplicar(a,b):
    print(a*b)

#  sumar,     restar,     multiplicar y     dividir.
# Debe permitir al usuario elegir el tipo de operación a realizar

# Preguntamos los numeros a operar
print('Ingresa los números')
num1 = int(input())
num2 = int(input())

# Preguntamos el tipo de operación que desea hacer
print('Ingresa el signo de la operación deseada. (+, -, %, *)')
signo = input()

resultado = 0

if signo == '+':
    sumar(num1,num2)
elif signo == '-':
    restar(num1,num2)
elif signo == '%':
    dividir(num1,num2)
elif signo == '*':
    multiplicar(num1,num2)

# DESARROLLADO POR: JUAN PABLO BAREÑO SIERRA I.T 1098677321

