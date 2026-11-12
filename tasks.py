def agregar_tarea(tareas, titulo, categoria="general"):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("El título es obligatorio")
    categoria = categoria.strip()
    if not categoria:
        raise ValueError("La categoría es obligatoria")
    tarea = {
        "id": max((t["id"] for t in tareas), default=0) + 1,
        "titulo": titulo,
        "categoria": categoria,
        "completada": False,
    }
    tareas.append(tarea)
    return tarea


def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea
    raise ValueError("Tarea no encontrada")


def eliminar_tarea(tareas, tarea_id):
    for indice, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            return tareas.pop(indice)
    raise ValueError("Tarea no encontrada")


def pendientes(tareas, categoria=None):
    resultado = [t for t in tareas if not t["completada"]]
    if categoria is not None:
        categoria = categoria.strip().casefold()
        resultado = [
            t for t in resultado
            if t.get("categoria", "").casefold() == categoria
        ]
    return resultado
