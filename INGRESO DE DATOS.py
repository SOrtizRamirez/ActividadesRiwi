#REALIZADO POR: Sharon R. Ortiz Ramírez
#Fecha: 23/04/2025

#Se define la función que hará la validación de campos
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
    
# Se pide el nombre del producto y se valida el campo
nombre = input("Digite el nombre del producto (solo texto): ") 
if es_numero(nombre):
    print("Error: No debe ingresar un número como nombre, reinicie el programa") #En caso de que no ingrese el nombre sino un número
else:
    cantidad = input("Digite la cantidad (Sólo números): ") #Se pide la cantidad
    if es_numero(cantidad): #Se valida la cantidad
     print("Cantidad válida")
     descuento = input("Digite el porcentaje de descuento (Sólo números sin símbolos): ") #Se pide el porcentaje
     if int(descuento) <= 100 and es_numero(descuento): 
       print("Descuento válido")
       precio = input("Digite el precio del producto (solo números): ") #Se pide el precio
       if es_numero(precio):
            precio = float(precio)
            print("Precio válido")
            if precio > 0:
             precio_total_und = int(cantidad) * int(precio) #en caso de que sea mayor a 0, se debe multiplicar la cantidad por el precio, generando una nueva variable
             if precio_total_und >= 0 : #Si la nueva variable es mayor a 0, significa que son más de 1 artículo
                        precio_total_desc = int (descuento) /100 #Se saca el porcentaje de descuento
             else:
                    print ("¡Error! La cantidad debe ser mayor a 0") #Se muestra el error en caso de que la cantidad sea 0
             if precio_total_desc > 0: #Se inicia la validación del total del descuento, en caso de que exista
                        precio_total_desc = precio_total_und * precio_total_desc #Operación matemática para saber el precio total
                        total = precio_total_und - precio_total_desc #Se hace la resta del descuento al total
                        print (f"El valor a pagar del artículo {nombre} es de {precio_total_und} usted ahorró {precio_total_desc}, total a pagar: {total} ") #Aquí se llaman a las variables para el mensaje final
             else:
                    print (f"Su artículo {nombre} no tiene descuento, el valor total es de: {precio_total_und}") #Aquí valor sin descuento
       else:
            print("Error: Debe ingresar un número") #Se empiezan a sacar los errores, es decir, los mensajes que se dirán cuando no digite bien
     else: 
        print("Error: No debe ingresar letras como descuento y un número menor a 100 y mayor a 0")
    else:
     print("Error: No debe ingresar letras como cantidad")




    
