print("Ejercicio 1")
nombre = input("Digita tu nombre: ")
edad = input("Digita tu edad: ")

print(f"Hola, tu nombre es {nombre} y tu edad es {edad}\n")

###################################################################################################################################

print("Ejercicio 2")

numero1 = int(input("Ingresa el número 1: "))
numero2 = int(input("Ingresa el número 2: "))

print(f"La suma es {numero1 + numero2}\n")

###################################################################################################################################

print("Ejercicio 3")

numero3 = float(input("Número decimal 1: "))
numero4 = float(input("Número decimal 2: "))

print (f"La multiplicación de los números decimales es de: {numero3*numero4}\n")

###################################################################################################################################

print("Ejercicio 4")

numero5 = int(input("Ingrese el número: "))
contador = int(input("¿Por cuál cantidad desea saber el múltiplo? "))

print (f"El {contador} de {numero5} es: {numero5*contador}\n")

###################################################################################################################################

print("Ejercicio 5")

palabra = input("Palabra a repetir: ")
contador2 = int(input("Número de veces a repetir la palabra: "))

print(palabra * contador2)

###################################################################################################################################

print("Ejercicio 6")

numero6 = int(input("Ingresa el primer número: "))
numero7 = int(input("Ingresa el segundo número: \n"))

print (numero6/numero7)

###################################################################################################################################

print("Ejercicio 7")

nombre1 = input("Digite su nombre: ")
cantidad1 = print(len(nombre1.replace(" ", "")))

###################################################################################################################################

print("Ejercicio 8")

numero8 = int(input("Digite el primer número: "))
numero9 = int(input("Digite el segundo número: "))

print(f"La división entera entre el {numero8} y {numero9} es de: {numero8//numero9}\nLa división entera en el orden contrario es de {numero9//numero8}\nEl módulo entre {numero8} y {numero9} es de: {numero8%numero9}\nEl módulo en el orden contrario es de {numero9%numero8}\n")

###################################################################################################################################

print("Ejercicio 9")

numero10 = int(input("Ingrese número 1: "))
numero11 = int(input("Ingrese número 2: "))

print(f"La suma es de {numero10+numero11}, la resta es de {numero10-numero11}, la multiplicación es de {numero10*numero11}, la división es de {numero10/numero11}.")

###################################################################################################################################

print("Ejercicio 10")

numero12 = int(input("Digite el número entero: "))

print(f"El numero{numero12} elevado a la 2 tiene como resultado {numero12^2} y a la 3 tiene como resultado {numero12^3}.")

###################################################################################################################################

print("Ejercicio 11")

numero13 = float(input("Ingrese un número decimal: "))

print(int(numero13))

###################################################################################################################################

print("Ejercicio 12")

edad1 = int(input("Ingrese su edad: "))
cambio = ("falso", "verdadero") [edad1>18]

print(f"Es {cambio} que su edad es mayor a 18")

####################################################################################################################################

print("Ejercicio 13")

numero14 = int(input("Ingrese el primer número: "))
numero15 = int(input("Ingrese el segundo número: "))
cambio1 = ("falso", "verdadero") [numero14 == numero15]

print(f"Es {cambio1} que los dos números son iguales.")

####################################################################################################################################

print("Ejercicio 14")

numero16 = int(input("Ingrese el primer número: "))
numero17 = int(input("Ingrese el segundo número: "))
cambio2 = ("falso", "verdadero") [numero16 > numero17]

print(f"Es {cambio2} que {numero16} es mayor que {numero17}.")

#####################################################################################################################################

print("Ejercicio 15")

numero18 = int(input("Ingrese el primer número: "))
numero19 = int(input("Ingrese el segundo número: "))
cambio3 = ("falso", "verdadero") [numero18 <= numero19]

print(f"Es {cambio3} que {numero18} es menor o igual que {numero19}.")

#####################################################################################################################################

print("Ejercicio 16")

numero20 = int(input("Ingrese el primer número: "))
numero21 = int(input("Ingrese el segundo número: "))
cambio4 = ("falso", "verdadero") [numero20 and numero21 > 10]

print(f"Es {cambio4} que {numero20} y {numero21} son mayores a 10.")

#####################################################################################################################################

print("Ejercicio 17")

numero22 = int(input("Ingrese el primer número: "))
numero23 = int(input("Ingrese el segundo número: "))
cambio5 = ("falso", "verdadero") [numero22 or numero23 > 10]

print(f"Es {cambio5} que {numero22} o {numero23} es mayor a 10")

#####################################################################################################################################

print("Ejercicio 18") 

numero24 = int(input("Ingrese el primer número: "))
numero25 = int(input("Ingrese el segundo número: "))
cambio6 = ("falso", "verdadero") [numero24 != numero25]

print(f"Es {cambio6} que {numero24} y {numero25} es son diferentes")

#####################################################################################################################################

print ("Ejercicio 19")


numero26 = int(input("Ingrese el primer número: "))
numero27 = int(input("Ingrese el segundo número: "))
numero28 = int(input("Ingrese el tercer número: "))
promedio = float(numero26+numero27+numero28)/3

print(promedio)

#####################################################################################################################################

print ("Ejercicio 20")

numero29 = int(input("Ingrese el número"))
divisible = ("falso", "verdadero") [(numero29 % 5) == 0]

print(f"Es {divisible} que {numero29} es divisible entre 5")
