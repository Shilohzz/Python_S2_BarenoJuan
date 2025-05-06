# Entrada: Queremos conocer los números a los cuáles sacaremos su promedio.
print('Ingresa un numero')
Num1 = float(input())
print('Ingresa un numero')
Num2 = float(input())
print('Ingresa un numero')
Num3 = float(input())

# Proceso: Tenemos que sumar todos los números que el usuario ingresa.
SumaNumeros = Num1 + Num2 + Num3
# Luego, dividimos ese resultado entre la cantidad de números que hay.
promedio = SumaNumeros / 3

# Salida: Queremos mostrar el promedio de los números ingresados.
print(promedio)
