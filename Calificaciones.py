#Hecho por: Sharon R. Ortiz Ramírez
#Fecha: 29/04/2025

#Se inicializan las variables necesarias
lista = []
promedio: float = 0
con: bool = True
promedio: float = 0
numero = float = 0

#Se pone un bucle While que tiene Fin cuando el usuario no desea agregar más calificaciones
while con:
    calificacion = int(input("Ingrese la nota a verificar: ")) #Aquí se pide agregar las calificaciones con un input
    if calificacion >= 0 and calificacion <= 100: #Se hace la validación de si las calificaciones son mayores o iguales a 0 y menores o iguales a 100
        if calificacion >= 65: #Aquí se habla de si la calificación es mayor o igual a 65, entonces debe aprobar, de lo contrario, no aprueba
            print("¡Aprobaste!")
            lista.append(calificacion)
        else:
            print("Reprobaste.")
            lista.append(calificacion)
        for i in range(len(lista)): #Este pequeño bucle For es para ir añadiendo esos números ingresados con anterioridad (siempre que el usuario diga que sí) a la lista
            i += 1
            promedio = sum(lista)/i #La variable promedio sería igual a la suma de la lista, dividido la cantidad de items en la lista
    else:
        print("La nota debe ser mayor o igual a 0 y menor o igual a 100.") #Este Else es para el error de si ingresan números negativos o mayores a 100   
    parar= input("¿Desea agregar más calificaciones? ") #Aquí se empieza a plantear el "freno" del While para que no sea un bucle infinito
    if parar.upper() == "SI" or parar.upper() == "SÍ": #Después se valida si el usuario desea agregar o no más calificaciones
        con = True #Si el usuario sí desea, entonces se continua con el bucle While
        print(lista) #Y se imprime la lista de los números que ha ingresado, siempre separados por coma.
    elif parar.upper() == "NO": #Si el usuario no desea, entonces 
        print("el promedio es de ", promedio, " de las calificaciones: ", lista) #Se imprime el promedio con la lista y
        con = False #Se frena el bucle While
    else: #Pero si entra cualquier otro valor que no está en sí o no
        con = False #Se frena el bucle While
        print("Error, debe ingresar Sí o No.") #Y saca error
temp  = 0 #Se inicializa la variable temporal que irá sumando las posiciones de la lista
numero = int(input("Ingrese el número a comparar: ")) #Se pide el número que desea comparar con las demás posiciones de la lista
for n in range(len(lista)): #Se hace que mientras haya números en la lista, la variable N continúe
    if numero > lista[n]: #si el número ingresado con anterioridad es mayor al número que está en la lista en la posición N, entonces
        print("El numero ", numero, "es mayor que ", lista[n], "que se encuentra en la posición ", n+1) #Número es mayor que 
    elif numero < lista[n]: #Si es menor que el número en la posición N, entonces
        print("El numero ", numero, "es menor que ", lista[n], "que se encuentra en la posición ", n+1) #Número es menor que
        temp = temp + 1 #Se van sumando los números mayores que el ingresado
    else:
        print("El numero ", numero, "es igual que ", lista[n], "que se encuentra en la posición ", n+1) #Y si número no es mayor ni menor, es porque es igual que
print("La cantidad de números mayores es de: ", temp) #Se imprimen la cantidad de números mayores.