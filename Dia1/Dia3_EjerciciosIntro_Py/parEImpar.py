# Queremos conocer el número que utilizaremos
print('Ingresa un número')
Num = int(input())

# Proceso: Para verificar que sea par, simplemente verificamos que el número al dividirse por 2, dé como resultado 0. Si es así, es par. Sino, no.
if Num % 2 == 0:
    print('El número es par')
else:
    print('El número es impar')