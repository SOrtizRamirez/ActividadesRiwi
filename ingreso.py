usuario_i = input("Ingrese el usuario:")
contraseña_i = input("Ingrese la contraseña:")
puerto = "3080"
bd = "prueba1"
servidor = (f"wwww.riwi.com/BD:{puerto}/{bd}/{usuario_i}&{contraseña_i}")

usuario = "sharizard"
contraseña = "ingreso20*"

servidor_si = "wwww.riwi.com/BD:3080/prueba1/sharizard&ingreso20*"

if servidor == servidor_si:
    print(servidor_si)

else:
    print("Intente nuevamente: Usuario y/o contraseña incorrectos.")