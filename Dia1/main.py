##############################################
############### Clase Dia 1 ##################
##############################################

#Imprimir en python
print("Hello World!")

#Creacion de variables
#1. Dato tipo string
nombre = "Pedro"
print(type(nombre))

#2. Dato tipo numero entero
numeroEntero=5
print(type(numeroEntero))

#3. Dato tipo numero real
numeroReal=5.3
print(type(numeroReal))

#4. Dato tipo double
numeroPi=3.1416345678909876345
print(type(numeroPi))

#5. Dato tipo booleano
booleano= False
print(type(booleano))

#6. (Solo Python) Numero complejo
numeroComplejo= complex('+1.23')
print(type(numeroComplejo))

#7.Convertir int a float
numeroNuevo = float(numeroEntero)
print(numeroNuevo)

#########################################################

#Ciclo for
for i in range(5):
    print(i)

print ("")

#(Desde-Hasta-Paso)
for i in range(1,5,1):
    print(i)

#########################################################

#Cilo While
boleanoNuevo=True
while(boleanoNuevo==True):
    print("Sigo siendo verdadero!")
    boleanoNuevo=False

#########################################################

#Condicionales if-else
texto="Corpus"
if(texto=="Corpus"):
    print("Sos corpus")
elif(texto=="Sharick"):
    print("Sos Sharick")
else:
    print("No sos ninguno")    

#########################################################

#Anidar condicionales
boolCorp1= True
boolCorp2= False
if(boolCorp1==True and boolCorp2==False):
    print("Todos somos verdaderos")
else:
    print("No somos iguales")

#########################################################

#Entradas de usuario

nombreUsuario = input("Â¿Cual es tu nombre?") #Todos los inpust son String
print("Tu nombre es :" + nombreUsuario)

edadUsuario= int(input("Cual es tu edad?"))
print("La edad de " + nombreUsuario + "es de: " + str(edadUsuario))

#########################################################

# 1. Funcion con retorno y con parametros

def areaCirculo(radio):
    valorPi=3.1416
    resultadoFinal = valorPi * (radio**2)
    return resultadoFinal
radioUsuario=float(input("Ingrese le radio del circulo: "))
print("El area del circulo es de: " + str(int(areaCirculo(radioUsuario))))

# 2. Funcion con retorno y sin parámetros
def valorDolar():
     return 4299
valorFinalDolar=valorDolar()
print("El valor del dólar es:"+str(valorFinalDolar))


#3. Función sin retorno y con parámetros
def concatenarNombres(nombre,apellido):
     print("Su nombre completo es:"+nombre+" "+apellido)
concatenarNombres("Sharick","Ibañez")


#4. Función sin retorno y sin parámetros
def funcionX():
     print("Soy una función que solo vive y existe")
funcionX()



# Desarrollado por : Juan Pablo Bareño Sierran / I.T 1098677321