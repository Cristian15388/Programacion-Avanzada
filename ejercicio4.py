def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def calcular_factorial(numero):
    if numero < 0:
        return "Error: Numero negativo no permitido."
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def contar_vocales(texto):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    texto = texto.lower()
    for char in texto:
        if char in vocales:
            vocales[char] += 1
    return vocales

def main():
    print("Seleccione una operacion:")
    print("1. Determinar si un numero es primo")
    print("2. Calcular factorial")
    print("3. Contar vocales en un texto")
    try:
        opcion = int(input("Ingrese la opcion (1/2/3): "))
    except ValueError:
        print("Error: Opcion invalida.")
        return

    if opcion == 1:
        try:
            numero = int(input("Ingrese el numero: "))
            print(f"El numero {numero} {'es' if es_primo(numero) else 'no es'} primo.")
        except ValueError:
            print("Error: Debe ingresar un numero entero.")
    elif opcion == 2:
        try:
            numero = int(input("Ingrese el numero: "))
            print(f"Factorial de {numero}: {calcular_factorial(numero)}")
        except ValueError:
            print("Error: Debe ingresar un numero entero.")
    elif opcion == 3:
        texto = input("Ingrese el texto: ")
        conteo = contar_vocales(texto)
        print("Conteo de vocales:")
        for vocal, count in conteo.items():
            print(f"{vocal}: {count}")
    else:
        print("Error: Opcion invalida.")

if __name__ == "__main__":
    main()