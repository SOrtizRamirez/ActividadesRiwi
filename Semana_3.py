#Hecho por: Sharon R. Ortiz Ramírez
#Fecha: 08/05/2025
import pandas as pd

# Function to upload products from excel
def upload_from_excel(archive="productos.xlsx"): #Here we named the function and called from excel
    try: #Here we said try the next block
        df = pd.read_excel(archive) #If we found the excel's product then
        return df #We return the data frame
    except FileNotFoundError: #else
        print("No se encontró el archivo. Se creará uno nuevo al guardar.") #Print an error and say we're going to created a new excel product
        return pd.DataFrame(columns=["nombre", "precio", "disponible"]) #With these columns

# Function to save products on excel   
def save_on_excel(df, archive="productos.xlsx"): #Here we are going to define a function for saving new data on the excel product
    df.to_excel(archive, index=False) #we save the dataframe in a excel product in the way "archivo", and we said we don't need a extra default column
    print(f"\nDatos guardados correctamente en '{archive}'.") #We print a message about a data successfully save on the excel product

#Function to edit 
def edit_on_excel(df, name): #We named the function
    product = df[df["nombre"] == name] #We searched it on excel
    if product.empty: #If the product is empty 
        print("Producto no encontrado.") #Product not finded
        return df #We return dataframe
    else: #But if we found it
        print(product) #We print the product with all the information
        wish: int = int(input("\n ¿Qué desea editar? \n1.Precio\n2.Cantidad disponible\nDigite el número de la opción: ")) #And we ask for what do you want to edit
        if wish == 1: #Option one
            new_price: float = float(input("Ingrese el nuevo precio: ")) #We ask for the new price
            df.loc[df["nombre"] == name, "precio"] = float(new_price) #and we change the price
            save_on_excel(df) #Saving on excel
            return df #We return the dataframe
        elif wish == 2:#option 2
            new_value: int = int(input("Ingrese la nueva cantidad disponible: ")) #We ask for the new value of quantity
            df.loc[df["nombre"] == name, "disponible"] = int(new_value) #We change the price
            save_on_excel(df) #We save on excel
            return df #And we return dataframe
        else: #Else is not 1 or 2
            print("Opción no válida.") #Option it's not avaliable
            return df #Return df
#Function for adding new products
def add_product(df, name):
    if name in df["nombre"].values: #First we check the product's name 
        wish: str = str(input("¡Error! El producto ya existe. ¿Desea modificarlo? ")) #If it does exist Want to change it?
        if wish.upper() in ["SÍ", "SI"]: #if yes
            edit_on_excel() #We call the function for editing
        elif wish.upper() == "NO": #if not
            return df #Always we return
    else: #Else it doesn't exist, we add it
        price: float = float(input("Ingrese el precio del nuevo producto: "))
        if price >= 150:
            value: int = int(input("Ingrese la cantidad disponible: "))
            if value >= 1:
                new_product = { 
                        "nombre": name,
                        "precio": price,
                        "disponible": value
                    }
                df = df._append(new_product, ignore_index=True)
                save_on_excel(df) 
                print(f"Producto'{name}' agregado correctamente.")
                return df
            else:
                print("¡Error! La cantidad disponible debe ser mayor o igual a 1")
                return df
        else:
            print("¡Error! El precio debe ser mayor a 150 pesos.")
            return df
            
#Function for searching products
def search_product(df, name):
    product = df[df["nombre"] == name]
    if product.empty:
        wish: str = str(input("Producto no encontrado. ¿Desea registrarlo?"))
        if wish.upper() in ["SÍ", "SI"]:
            add_product(df_products, name)
            return df
        elif wish.upper() == "NO":
            return df
        else:
            print("Opción no válida.")
        return df 
    else:
        print(product)

#Funtion for removing a product
def remove_product(df, name):
    if name.upper() in df["nombre"].values:
        sure:str = str(input("¿Está seguro que desea eliminar el producto? ")).upper()
        if sure in ["SÍ", "SI"]: 
            df = df[df["nombre"] != name] 
            save_on_excel(df)
            return df 
            print(f"Producto '{name}' eliminado correctamente.") 
        else:
            print(f"Producto '{name}' no ha sido eliminado.")
            return df
    else:
        print("Producto no encontrado.")
        return df

#Function for checking costs
def check_cost(df):
    total:float = 0 #We start with the total cost in zero
    for _, product in df.iterrows(): #We roam on the excel's product in each row
        subtotal:float = float(product["disponible"] * product["precio"]) #subtotal is the var that is going to multiply the available count and the count of replacement
        print(f"{product['nombre']}: {subtotal} pesos") #we are going to print every product's  subtotal
        total += subtotal #And we add up to total
    print(f"\nCosto total de reposición de todos los productos: {total} pesos")

df_products = upload_from_excel()

# Menu
while True: #We are going to execute the menu 
    print("\n")
    print("                 ──── ୨୧ ────𝐖𝐄𝐋𝐂𝐎𝐌𝐄──── ୨୧ ────")
    print("════════════════════════════ ＭＥＮÚ ═══════════════════════════")
    print("════════════════════════════════════════════════════════════════")
    print("═════════════¿ＱＵÉ ＤＥＳＥＡＳ ＨＡＣＥＲ ＨＯＹ？════════════\n")
    print("Para buscar un producto: B          │")
    print("Para eliminar un producto: E        │")
    print("Para registrar un nuevo producto: R │")
    print("Para ver costos totales: C          │")
    print("Para cambiar el costo de un p.: P   │")
    print("Para salir: S                       │\n")
    menu: str = input("Digite la letra que corresponde a la opción deseada: ")
    
    if menu.upper() == "B": #Is user want to search
        name: str = str(input("Ingrese el nombre del producto que desea buscar: ")).upper() #We ask for the information
        search_product(df_products, name) #We call the function for searching
    elif menu.upper() == "E": #If user want to errase a product
        name: str = input("Ingrese el nombre del producto que desea eliminar: ").upper() #We ask for the product we are going to remove from inventary
        df_products = remove_product(df_products, name) #We call the function for errasing
    elif menu.upper() == "R": #if user want to add new products
        name: str = str(input("Ingrese el nombre del nuevo producto: ")).upper()
        df_products = add_product(df_products, name) #We call the function for registering
    elif menu.upper() == "C": #If user said that want to see the costs
        check_cost(df_products) #We call the function for costs
    elif menu.upper() == "P":
        name: str = str(input("Ingrese el nombre del producto que desea editar: ")).upper()
        edit_on_excel(df_products, name)
    elif menu.upper() == "S": #If the user want to scape 
        save_on_excel(df_products) #We save all we did
        break #And close the program
    else:
        print("Opción no válida.") #Error message if user doesn't writ
