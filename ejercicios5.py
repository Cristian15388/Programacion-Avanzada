def validar_y_obtener_datos():
    while True:
        nombre = input("Ingrese el nombre: ")
        if len(nombre) >= 3:
            break
        print("Error: Nombre debe tener minimo 3 caracteres. Intente nuevamente.")

    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if 0 <= edad <= 120:
                break
            print("Error: Edad debe estar entre 0 y 120. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un numero entero. Intente nuevamente.")

    while True:
        correo = input("Ingrese el correo: ")
        if '@' in correo and (correo.endswith('.com') or correo.endswith('edu.co')):
            break
        print("Error: Correo debe contener '@' y terminar en '.com' o 'edu.co'. Intente nuevamente.")

    return {"nombre": nombre, "edad": edad, "correo": correo}

def main():
    
    lista_datos = []

    
    datos = validar_y_obtener_datos()
    lista_datos.append(datos)

    
    print("Informacion almacenada:")
    print(lista_datos)

if __name__ == "__main__":
    main()
