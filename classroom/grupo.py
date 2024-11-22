from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes = None):
        self._grupo = grupo
        if asignaturas == None:
            self._asignaturas = []
        else:
            self._asignaturas = asignaturas
        
        if estudiantes == None:
            self.listadoAlumnos = []
        else:
            self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for value in kwargs.values():
            self._asignaturas.append(Asignatura(value))

    def agregarAlumno(self, alumno, lista=None):
        if lista == None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        mensaje = "Grupo de estudiantes: " + self._grupo
        return mensaje

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

