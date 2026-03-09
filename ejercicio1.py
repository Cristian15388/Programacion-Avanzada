def main():
    # Lista de estudiantes (estructuras como diccionarios)
    estudiantes = [
        {
            "nombre": "Juan Perez",
            "edad": 20,
            "estado": "activo",
            "materias": ["Matematicas", "Ciencias", "Historia"],
            "notas": {"Matematicas": 4.5, "Ciencias": 3.2, "Historia": 4.0}
        },
        {
            "nombre": "Maria Lopez",
            "edad": 22,
            "estado": "inactivo",
            "materias": ["Fisica", "Quimica", "Biologia", "Ingles"],
            "notas": {"Fisica": 2.8, "Quimica": 3.5, "Biologia": 4.1, "Ingles": 3.0}
        }
    ]

    for estudiante in estudiantes:
        # Validaciones
        if len(estudiante["materias"]) < 3:
            print(f"Error para {estudiante['nombre']}: Debe tener al menos 3 materias.")
            continue
        for materia, nota in estudiante["notas"].items():
            if not (0.0 <= nota <= 5.0):
                print(f"Error para {estudiante['nombre']}: Nota invalida en {materia} ({nota}).")
                continue

        # Calculos
        notas = estudiante["notas"]
        promedio = sum(notas.values()) / len(notas)
        mejor_materia = max(notas, key=notas.get)
        peor_materia = min(notas, key=notas.get)
        aprueba = promedio >= 3.0

        # Mostrar resultados
        print(f"Estudiante: {estudiante['nombre']}")
        print(f"Promedio general: {promedio:.2f}")
        print(f"Materia con mejor nota: {mejor_materia} ({notas[mejor_materia]})")
        print(f"Materia con peor nota: {peor_materia} ({notas[peor_materia]})")
        print(f"Aprueba: {'Si' if aprueba else 'No'}")
        print("---")

if __name__ == "__main__":
    main()