from tasks import agregar_tarea, completar_tarea, pendientes

tareas = []
agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")
agregar_tarea(tareas, "Preparar laboratorio", "Trabajo")
agregar_tarea(tareas, "Revisar apuntes", "Estudio")
completar_tarea(tareas, 1)

print("Pendientes:")
for tarea in pendientes(tareas):
    print(f'- {tarea["id"]}: {tarea["titulo"]} [{tarea["categoria"]}]')

print("Pendientes de estudio:")
for tarea in pendientes(tareas, "estudio"):
    print(f'- {tarea["id"]}: {tarea["titulo"]} [{tarea["categoria"]}]')
