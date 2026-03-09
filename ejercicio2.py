def main():

    try:
        valor_base = float(input("Ingrese el valor monetario: "))
    except ValueError:
        print("Error: Debe ingresar un numero valido.")
        return

    
    impuesto = valor_base * 0.19
    descuento = valor_base * 0.10 if valor_base >= 200000 else 0
    total_final = valor_base + impuesto - descuento

    
    print(f"Valor base: {valor_base}")
    print(f"Impuesto (19%): {impuesto}")
    print(f"Descuento (10% si >= 200000): {descuento}")
    print(f"Total final: {total_final}")

if __name__ == "__main__":
    main()
