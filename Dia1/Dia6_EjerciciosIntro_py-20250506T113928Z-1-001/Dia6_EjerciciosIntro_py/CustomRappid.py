print("Digite el numero de hamburguesas a pedir:  ")
N = int(input())  # Corrige la entrada de N

subtotal = 0  # Inicializa la variable subtotal

for i in range(N):
    print('')
    print("Ingredientes para la hamburguesa No.: ", i + 1)  # Ajusta el índice para que inicie en 1
    print('')

    while True:  # Corrige la condición del bucle
        print("Seleccione el tipo de pan: ")
        print("1. Centeno valor de - 1000")
        print("2. Avena - 1500")
        pan = int(input())  # Cambia a int para comparar correctamente
        if pan == 1:
            subtotal = subtotal + 1000
            break
        elif pan == 2:
            subtotal = subtotal + 1500
            break

    while True:
        print("Seleccione el tipo de carne: ")
        print("1. 250G - 5000")
        print("2. 300G - 7500")
        carne = int(input())
        if carne == 1:
            subtotal = subtotal + 5000
            break
        elif carne == 2:
            subtotal = subtotal + 7500
            break

    while True:
        print("Seleccione el tipo de pollo: ")
        print("1. 250G - 4500")
        print("2. 350G - 5500")
        pollo = int(input())
        if pollo == 1:
            subtotal = subtotal + 4500
            break
        elif pollo == 2:
            subtotal = subtotal + 5500
            break

    while True:
        print("Seleccione el tipo de pollo desmechado: ")
        print("1. 250G - 1000")
        print("2. 350G - 1500")
        pollo_des = int(input())
        if pollo_des == 1:
            subtotal = subtotal + 6500
            break
        elif pollo_des == 2:
            subtotal = subtotal + 7500
            break

    while True:
        print("Seleccione el tipo de tocineta: ")
        print("1. 1 Lonja - 1500")
        print("2. 2 Lonjas - 2500")
        tocineta = int(input())
        if tocineta == 1:
            subtotal = subtotal + 1500
            break
        elif tocineta == 2:
            subtotal = subtotal + 2500
            break

    while True:
        print("Seleccione el tipo de papa frita: ")
        print("1. A la francesa - 5000")
        print("2. En cascos - 6000")
        papa_frita = int(input())
        if papa_frita == 1:
            subtotal = subtotal + 5000
            break
        elif papa_frita == 2:
            subtotal = subtotal + 6000
            break

    while True:
        print("Seleccione el tipo de bebida: ")
        print("1. Gaseosa - 5000")
        print("2. Club Colombia - 8000")
        print("3. Naranjada - 9000")
        bebida = int(input())
        if bebida == 1:
            subtotal = subtotal + 5000
            break
        elif bebida == 2:
            subtotal = subtotal + 8000
            break
        elif bebida == 3:
            subtotal = subtotal + 9000
            break

servicio = subtotal * 0.1
total = subtotal + servicio

print("El valor del subtotal es de: ", subtotal)
print("El valor del servicio es de: ", servicio)
print("El valor total es de: ", total)




