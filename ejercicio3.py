def main():
    # Ingresar dos numeros enteros por teclado
    try:
        num1 = int(input("Ingrese el numero de inicio para la serie Fibonacci: "))
        num2 = int(input("Ingrese el numero de iteraciones (terminos): "))
    except ValueError:
        print("Error: Debe ingresar numeros enteros validos.")
        return

    # Si el limite (num2) es negativo, error
    if num2 < 0:
        print("Error: El limite no puede ser negativo.")
        return

    # Generar la serie Fibonacci starting from num1 (asumiendo secuencia como  num1 como F1=F2, o con previo 0)
    serie = []
    if num2 > 0:
        serie.append(num1)
        a, b = 0, num1
        for _ in range(1, num2):
            c = a + b
            a = b
            b = c
            serie.append(c)

    # Mostrar resultados
    print(f"La lista completa generada: {serie}")
    print(f"Cuantos terminos se generaron: {len(serie)}")
    if serie:
        print(f"El ultimo valor incluido: {serie[-1]}")
    else:
        print("No se generaron terminos.")

if __name__ == "__main__":
    main()