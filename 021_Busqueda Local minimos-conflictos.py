import random  # Importa el módulo random para generar números aleatorios

def asignar_proyectos(estudiantes, proyectos, max_iter):
    # Inicializa la asignación de estudiantes a proyectos de manera aleatoria
    asignaciones = {estudiante: random.choice(proyectos) for estudiante in estudiantes}
    
    for _ in range(max_iter):  # Itera hasta alcanzar el número máximo de iteraciones
        conflicto_estudiante = None
        for estudiante in estudiantes:
            # Encuentra un estudiante que esté en conflicto, es decir, que comparta proyecto con otro estudiante
            if sum(1 for otro_estudiante in estudiantes if asignaciones[otro_estudiante] == asignaciones[estudiante]) > 1:
                conflicto_estudiante = estudiante
                break
        
        if conflicto_estudiante is None:
            # Si no hay conflictos, devuelve la asignación
            return asignaciones
        
        # Resuelve el conflicto cambiando al estudiante a otro proyecto aleatorio
        proyecto_actual = asignaciones[conflicto_estudiante]
        proyectos_disponibles = [p for p in proyectos if p != proyecto_actual]
        asignaciones[conflicto_estudiante] = random.choice(proyectos_disponibles)
    
    # Si no se encuentra una solución en el número máximo de iteraciones, devuelve None
    return None

# Ejemplo de uso
estudiantes = ["Estudiante1", "Estudiante2", "Estudiante3", "Estudiante4", "Estudiante5"]
proyectos = ["ProyectoA", "ProyectoB", "ProyectoC"]

# Asigna los estudiantes a proyectos utilizando la búsqueda local de mínimos conflictos
resultado = asignar_proyectos(estudiantes, proyectos, max_iter=1000)

if resultado:
    print("Asignación de estudiantes a proyectos:")
    for estudiante, proyecto in resultado.items():
        print(f"{estudiante} -> {proyecto}")
else:
    print("No se encontró una solución en el número máximo de iteraciones.")
