# Creador de examenes

class Persona:
    def __init__(self, nombre, apellido, dni, contraseña,tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.contraseña = contraseña
        self.tipo = tipo
        self.alumnos = []
        self.profesores = []

    def loguearse(self, dni, contraseña):
        pass

class Profesor(Persona):
    def __init__(self, nombre, apellido, __dni, __contraseña, tipo, asignatura):
        super().__init__(nombre, apellido, __dni, __contraseña, tipo)
        self.asignatura = asignatura

    def loguearse(self):
        pass

    def crear_examen(self):
        pass

class Alumno(Persona):
    def __init__(self, nombre, apellido, __dni, __contraseña, tipo):
        super().__init__(nombre, apellido, __dni, __contraseña, tipo)

    def loguearse(self):
        pass

    def realizar_examen(self):
        pass

class Examen:
    def __init__(self, asignatura, puntuacion):
        
        self.consignas = []
        self.asignatura = asignatura
        self.puntuacion = puntuacion

class Pregunta:
    def __init__(self, puntuacion, respuesta, descripcion):
        
        self.puntuacion = puntuacion
        self.respuesta = respuesta
        self.descripcion = descripcion

    def obtener_descripcion(self):
        pass

    def evaluar_respuesta(self, respuesta):
        pass

class PreguntaOpcionMultiple(Pregunta):
    pass

class PreguntaVerdaderoFalso(Pregunta):
    pass

class PreguntaAbierta(Pregunta):
    pass

class Sistema:
    pass
