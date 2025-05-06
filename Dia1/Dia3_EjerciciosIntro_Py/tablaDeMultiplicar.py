# Entrada: Queremos conocer el número que utilizaremos para la tabla.
print('Ingresa un numero: ')
Num = int(input())

# Proceso: Necesitamos crear un bucle que multiplique el número recibido, desde 1 hasta 10, y lo imprima por separado.
for inicio in range(1, 11):
    Tabla = Num * inicio
    print(f'{Num} x {inicio} = {Tabla}')