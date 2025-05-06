# Verificar si un número es primo o no. (Primos, son aquellos que tienen como divisores solamente el 1 y él mismo)

# Queremos conocer cuál es el número por verificar.
print('Ingresa un número')
Num = int(input())

contador = 0

# Proceso: Debemos crear un bucle que divida el número ingresado por todos los números que hay desde 1 hasta él mismo.
# Si el número es divisible solo por dos números (1 y él mismo) es primo, sino no.
for bucle in range(1, Num + 1):
    if Num % bucle == 0:
        contador = contador + 1

# Salida: Queremos ver si es primo o no. Para esto, comprobamos que el número se haya podido dividir exactamente solo con 2 números.
if contador == 2:
    print('El número', Num, 'es primo')
else:
    print('El número', Num, 'no es primo')