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
    resultado = num1 + num2
elif signo == '-':
    resultado = num1 - num2
elif signo == '%':
    resultado = num1 / num2
elif signo == '*':
    resultado = num1 * num2

print(f'El resultado de tu operación es {resultado}.')

# DESARROLLADO POR: JUAN PABLO BAREÑO SIERRA I.T 1098677321