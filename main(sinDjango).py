# main.py
from jim_app.models import Usuario, Curso, Matricula, Ejercicio, Valoracion

# Crear algunos usuarios
usuario1 = Usuario("Pab", "Paz", "pab@email.com", "Socio")
usuario2 = Usuario("Bap", "Pez", "bap@email.com", "Entrenador")
usuario3 = Usuario("Los", "Mar", "losemail.com", "Socio")

# Crear un curso
curso_spinning = Curso("Spinning Avanzado", "Curso de spinning para nivel avanzado", "Spinning", usuario2, 20)

# Matricular socios en el curso
matricula1 = Matricula(curso_spinning, usuario1)
matricula2 = Matricula(curso_spinning, usuario3)

# Crear un ejercicio
ejercicio1 = Ejercicio("Bicicleta Estática", "Ejercicio en bicicleta estática", "Piernas")

# Crear una valoración
valoracion1 = Valoracion(curso_spinning, usuario1, 4, "Muy buen curso, aunque algo.")
valoracion2 = Valoracion(curso_spinning, usuario3, 5, "Excelente curso. El mejor que he tomado.")

# Imprimir los objetos para ver cómo funcionan
print(usuario1)
print(usuario2)
print(curso_spinning)
print(matricula1)
print(matricula2)
print(ejercicio1)
print(valoracion1)
print(valoracion2)
