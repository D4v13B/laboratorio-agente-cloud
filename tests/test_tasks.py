import unittest
from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes


class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertFalse(tarea["completada"])

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_agregar_tarea_con_categoria(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "  Estudio  ")
        self.assertEqual(tarea["categoria"], "Estudio")

    def test_agregar_tarea_categoria_vacia(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Leer documentación", "")
        self.assertEqual(tareas, [])

    def test_agregar_tarea_categoria_solo_espacios(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Leer documentación", "   ")
        self.assertEqual(tareas, [])

    def test_pendientes_filtra_por_categoria(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Enviar informe", "Trabajo")
        agregar_tarea(tareas, "Repasar apuntes", "estudio")
        completar_tarea(tareas, 3)
        resultado = pendientes(tareas, "ESTUDIO")
        self.assertEqual([t["id"] for t in resultado], [1])

    def test_pendientes_categoria_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Enviar informe", "Trabajo")
        self.assertEqual(pendientes(tareas, "Ocio"), [])

    def test_pendientes_sin_categoria_devuelve_todas(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Enviar informe", "Trabajo")
        self.assertEqual(len(pendientes(tareas)), 2)

    def test_eliminar_tarea_existente(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación")
        agregar_tarea(tareas, "Enviar informe")
        eliminada = eliminar_tarea(tareas, 1)
        self.assertEqual(eliminada["titulo"], "Leer documentación")
        self.assertEqual([t["id"] for t in tareas], [2])

    def test_eliminar_tarea_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación")
        copia = [dict(t) for t in tareas]
        with self.assertRaisesRegex(ValueError, "Tarea no encontrada"):
            eliminar_tarea(tareas, 99)
        self.assertEqual(tareas, copia)

    def test_id_no_se_repite_tras_eliminar(self):
        tareas = []
        agregar_tarea(tareas, "A")
        agregar_tarea(tareas, "B")
        eliminar_tarea(tareas, 1)
        tarea_c = agregar_tarea(tareas, "C")
        self.assertEqual(tarea_c["id"], 3)


if __name__ == "__main__":
    unittest.main()
