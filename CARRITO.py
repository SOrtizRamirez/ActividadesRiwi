cantidad = int(input("¿Cuántos productos va a llevar el cliente? (rango 1 a 4): "))
pago = print("¿Pagará con tarjeta? ")
if cantidad > 0:
    if cantidad == 1:
        nombre = input("Digite el nombre del producto: ")
        precio = float(input("Digite el precio: "))
        if precio > 50000:
                print (f"Su producto {nombre} tiene un valor de {precio} si decide pagar en efectivo{precio - (precio*0.05)} \nSi decide pagar con ")
        elif precio < 100000 and precio > 50000:
                print (f"Su producto {nombre} tiene un valor de {precio} ")
        else:
            print (f"Su producto {nombre} tiene un valor de {precio}")
    elif cantidad == 2:
        nombre = input("Digite el nombre del primer producto: ")
        nombre1 = input (f"Digite el segundo producto: ")
        precio = float(input("Digite el precio: "))
        precio1= float(input("Digite el segundo precio: "))
        if pago == "Sí" or "Si":
            if precio + precio1 > 50000:
                print (f"Sus productos {nombre}, {nombre1} tiene un valor de {precio+precio1}")
            elif precio + precio1 > 100000:
                print (f"Sus productos {nombre}, {nombre1}  usted tiene 2% de cashback ({((precio + precio1)*0.02)})")
        else:
            print (f"Su producto {nombre}, {nombre1} tiene un valor de {precio + precio1}")
    elif cantidad == 3:
        nombre = input("Digite el nombre del primer producto: ")
        nombre1 = input (f"Digite el segundo producto: ")
        nombre2 = input (f"Digite el tercer producto: ")
        precio = float(input("Digite el precio: "))
        precio1= float(input("Digite el segundo precio: "))
        precio2= float(input("Digite el tercer precio: "))
        print (f"Sus productos {nombre}, {nombre1}, {nombre2} tiene un valor de {precio+precio1+precio2}")
    elif cantidad == 4:
        nombre = input("Digite el nombre del primer producto: ")
        nombre1 = input (f"Digite el segundo producto: ")
        nombre2 = input (f"Digite el tercer producto: ")
        nombre3 = input ("Digite el nombre del cuarto producto: ")
        precio = float(input("Digite el precio: "))
        precio1= float(input("Digite el segundo precio: "))
        precio2= float(input("Digite el tercer precio: "))
        precio3= float(input("Digite el cuarto precio: "))
        print (f"Sus productos {nombre}, {nombre1}, {nombre2}, {nombre3} tiene un valor de {precio+precio1+precio2+precio3}")
    elif cantidad == 5:
        nombre = input("Digite el nombre del primer producto: ")
        nombre1 = input (f"Digite el segundo producto: ")
        nombre2 = input (f"Digite el tercer producto: ")
        nombre3 = input ("Digite el nombre del cuarto producto: ")
        nombre4 = input("Digite el nombre del quinto producto: ")
        precio = float(input("Digite el precio: "))
        precio1= float(input("Digite el segundo precio: "))
        precio2= float(input("Digite el tercer precio: "))
        precio3= float(input("Digite el cuarto precio: "))
        precio4= float(input("Digite el quinto precio: "))
        print (f"Sus productos {nombre}, {nombre1}, {nombre2}, {nombre3} y {nombre4} tiene un valor de {precio+precio1+precio2+precio3+precio4}")
else:
        print("La cantidad de productos debe ser mayor a 0 y menor o igual a 5.")


