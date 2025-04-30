#Hecho por: Sharon R. Ortiz Ramírez
#Fecha: 29/04/2025

#Se declaran las variables y su tipo
texto: str = ""
lista1: str = ""
concatenar: float = 0
lista: list = []
tempo: int = 0
temp:int = 0
parar = True

while parar:
    lista1: str = input("Ingrese la lista de calificaciones separadas por coma (,), recuerde terminar con la coma (,): ") #Se pide que ingrese los datos
    numero1 = int(input("Ingrese el número a comparar: ")) #Ingreso de datos 2.
    for i in lista1: #Se inicia el bucle for para añadir los números a la lista
        if i != ",": #Mientras la variable i sea diferente de , entonces
            texto = texto.__add__(i) #Se concatenan o se añaden los valores a i     
        else: #si no se cumple la condición
            numero: float = float (texto) #se declara la variable número para agarrar la información que contiene texto
            concatenar = concatenar + float(numero) #Se concatenan los números y luego se cambian a float
            lista.append(numero) #Se añade lo que contiene número a la lista
            texto = "" #Se vacía texto
            temp += 1 #Se cuentan cuántas , hay para posteriormente utilizar el valor para el promedio
            i = int() #Se vuelve i a entero

    for n in range(len(lista)): #Se inicia bucle for para saber cuántos números de la LISTA son 
        if numero1 > lista[n]: #Mayores que el número ingresado con anterioridad
            tempo += 1 #Otra variable que contará cuántos números tenemos, pero esta vez menores.
    if numero >= 0 and numero <= 100:
        parar = True
        print("Calificaicones válidas.")
    else:
        parar = False 
        print("Calificaciones inválidas, deben ser mayores o iguales a 0 y menores o iguales a 100. El programa se cerrará.")
        break

    promedio = concatenar/(temp) #Se saca el promedio
    print("El promedio de las calificaciones ingresadas es de: ", promedio) #Se imprime el promedio
    print("La cantidad de números menores es de: ", tempo) #Se imprime la cantidad de números menores

    if promedio > 65: #Se mira si el estudiante aprueba o no
        print("¡Aprobado! Felicitaciones") #En caso de aprobar
    else:
        print("Desaprobado.") #En caso de no aprobar
    desea = input("¿Desea ingresar las calificaciones de otro estudiante? ") #Se interactúa con el usuario por si desea ingresar más calificaciones
    if desea.upper() == "SI" or desea.upper() == "SÍ": #Si el usuario responde que sí
        parar = True #Entonces el programa continúa de nuevo desde 0
    else: #En caso de No
        parar = False #El programa se detiene
        print("¡Gracias por elegirnos! Nos vemos luego. El programa se cerrará automáticamente.") #Mensaje de despedida.