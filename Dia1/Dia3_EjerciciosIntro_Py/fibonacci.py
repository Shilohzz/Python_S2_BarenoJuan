# Entrada: Queremos conocer el número que usaremos para la serie de Fibonacci.
print("Ingresa un número: ")
Num = int(input())

# Proceso: Primero asignamos los dos valores iniciales de la serie Fibonacci (0 y 1. Acá arranca todo)
f0 = 0
f1 = 1

# Proceso/Salida: Parte del proceso es crear el bucle para que itere entre los dos números anteriores para conocer el siguiente.
# Adicional, también queremos que vaya mostrando la serie de Fibonacci hasta el número que indicamos.
for i in range(1, Num + 1):
    print(f0)
    fa = f0 + f1
    f0 = f1
    f1 = fa