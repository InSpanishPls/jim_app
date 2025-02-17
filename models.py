from datetime import datetime
from typing import Optional

# Definir la clase Usuario
class Usuario:
    def __init__(self, nombre: str, apellidos: str, email: str, tipo: str):
        """
        Constructor para crear un nuevo usuario.
        :param nombre: Nombre del usuario
        :param apellidos: Apellidos del usuario
        :param email: Correo electrónico del usuario
        :param tipo: Tipo de usuario ('Administrador', 'Entrenador', 'Socio')
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.fecha_registro = datetime.now()  # Fecha de registro
        self.tipo = tipo  # Tipo de usuario (Administrador, Entrenador, Socio)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.tipo})"

# Definir la clase Curso
class Curso:
    def __init__(self, titulo: str, descripcion: str, tipo_curso: str, entrenador: Usuario, capacidad_maxima: int):
        """
        Constructor para crear un nuevo curso.
        :param titulo: Título del curso
        :param descripcion: Descripción del curso
        :param tipo_curso: Tipo de curso (Spinning, Pilates)
        :param entrenador: Entrenador que imparte el curso (instancia de Usuario)
        :param capacidad_maxima: Capacidad máxima de participantes en el curso
        """
        self.titulo = titulo
        self.identificador = titulo.replace(" ", "-").lower()  # Convertir el título en un identificador único (Slug)
        self.descripcion = descripcion
        self.entrenador = entrenador  # Relación con el entrenador (Usuario)
        self.fecha_creacion = datetime.now()  # Fecha de creación del curso
        self.capacidad_maxima = capacidad_maxima
        self.tipo_curso = tipo_curso  # Tipo de curso (Spinning, Pilates)

    def __str__(self):
        return self.titulo

# Definir la clase Matricula
class Matricula:
    def __init__(self, curso: Curso, socio: Usuario):
        """
        Constructor para crear una matrícula de un socio en un curso.
        :param curso: Curso al que se matricula el socio
        :param socio: Socio que se está matriculando (instancia de Usuario)
        """
        self.curso = curso  # Relación con el curso
        self.socio = socio  # Relación con el socio (Usuario)
        self.fecha_matricula = datetime.now()  # Fecha en que el socio se matricula

    def __str__(self):
        return f"{self.socio.nombre} {self.socio.apellidos} - {self.curso.titulo}"

# Definir la clase Ejercicio
class Ejercicio:
    def __init__(self, nombre: str, descripcion: str, grupo_muscular: str):
        """
        Constructor para crear un ejercicio.
        :param nombre: Nombre del ejercicio
        :param descripcion: Descripción del ejercicio
        :param grupo_muscular: Grupo muscular al que pertenece el ejercicio
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.grupo_muscular = grupo_muscular  # Grupo muscular al que pertenece el ejercicio

    def __str__(self):
        return f"{self.nombre} ({self.grupo_muscular})"

# Definir la clase Valoracion
class Valoracion:
    def __init__(self, curso: Curso, socio: Usuario, puntuacion: int, comentario: Optional[str] = None):
        """
        Constructor para crear una valoración de un curso hecha por un socio.
        :param curso: Curso que está siendo valorado
        :param socio: Socio que hace la valoración
        :param puntuacion: Puntuación (de 1 a 5)
        :param comentario: Comentario adicional (opcional)
        """
        self.curso = curso  # Relación con el curso
        self.socio = socio  # Relación con el socio (Usuario)
        self.puntuacion = puntuacion  # Puntuación (de 1 a 5)
        self.comentario = comentario  # Comentario opcional
        self.fecha_creacion = datetime.now()  # Fecha de la creación de la valoración

    def __str__(self):
        return f"Valoración de {self.socio.nombre} para {self.curso.titulo}: {self.puntuacion}/5"
