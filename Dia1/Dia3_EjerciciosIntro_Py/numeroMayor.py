# Entrada: Queremos conocer los tres números para comparar
print('Ingresa un número')
Num1 = float(input())
print('Ingresa otro número')
Num2 = float(input())
print('Ingresa otro número')
Num3 = float(input())

# Proceso: Ahora queremos comparar los números para saber cuál es mayor entre los tres.
# Creamos una condición que nos permita comparar el número 1 con el número 2. Si el número 1 es mayor,
# Compararemos después el número 1 con el 3. Sino, Comparamos el número 2 con el 3.
if Num1 > Num2:
    temp = Num1
else:
    temp = Num2
    if temp > Num3:
        temp = temp
    else:
        temp = Num3

# Salida: Queremos mostrar el número mayor según el análisis del proceso.
print(temp)
