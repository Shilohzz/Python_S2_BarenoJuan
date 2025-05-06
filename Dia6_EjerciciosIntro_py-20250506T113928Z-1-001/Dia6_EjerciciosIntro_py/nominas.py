print('Bienvenido! Agente de nominas, por favor ingrese la cantidad de empleados')
numEmpleados = int(input())
valorHora = 20000
totalBruto = 0
totalEps = 0
totalNeto = 0
totalPension = 0
maxNeto = 0
minNeto = 0

for iterador in range(numEmpleados):
    print('Ingrese el nombre del empleado: ')
    nombres = input()
    print(f'¿Cuantas horas ha trabajado {nombres}?')
    horasTrabajadas = int(input())

    salarioBruto = horasTrabajadas * valorHora
    EPS = salarioBruto * 0.04
    Pension = salarioBruto * 0.04

    salarioNeto = salarioBruto - EPS - Pension
    totalBruto += salarioBruto
    totalEps += EPS
    totalPension += Pension
    totalNeto += salarioNeto

    print(f'El sueldo bruto del empleado {nombres} es: {salarioBruto}')
    print(f'El sueldo bruto menos EPS del empleado {nombres} es: {EPS}')
    print(f'El sueldo bruto menos la pension del empleado {nombres} es: {Pension}')
    print(f'El sueldo neto del empleado {nombres} es: {salarioNeto}')
    print('===============================================================')
    print('')

    if salarioNeto > maxNeto:
        nombreMenor = nombreMayor if 'nombreMayor' in locals() else ''
        minNeto = maxNeto
        maxNeto = salarioNeto
        nombreMayor = nombres

    if salarioNeto < minNeto or minNeto == 0:
        minNeto = salarioNeto
        nombreMenor = nombres

print('===============================================================')
print('')
print('TOTALES')

print(f'El empleado con mayor salario es: {nombreMayor} ${maxNeto}')
print(f'El empleado con menor salario es: {nombreMenor} ${minNeto}')
print(f'El total de salarios brutos es: {totalBruto}')
print(f'El total recaudado por la EPS es: {totalEps}')
print(f'El total recaudado por Pension es: {totalPension}')
print(f'El total de salarios netos es: {totalNeto}')
