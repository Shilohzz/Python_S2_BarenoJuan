factorial = 1
# Entrada: Queremos conocer el número que vamos a fraccionar
print('Ingresa un numero')
Num1 = int(input())

# Proceso: Creamos un bucle for, para que se multiplique el número ingresado por sí mismo y todos los anteriores a él.
for i in range(1, Num1 + 1):
    factorial = factorial * i

# Salida: Queremos mostrar el resultado en pantalla, para ello imprimimos el resultado final de nuestro bucle.
print('El resultado es: ', factorial)
