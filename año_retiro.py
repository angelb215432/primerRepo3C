#Este programa calcula la edad y anio de retiro de una persona dadas su edad actual y la edad a la que se quiere retirar
# Hoy es 4 de Octubre de 2021
# 1. Inicio
# 2. Definir anio_actual = 2021
anio_actual = 2021
# 3. Preguntar al usuario = "¿Qué edad tienes?"
print("Que edad tienes?")
# 4. Definir edad_actual = entrada del usuario
edad_actual = int(input()) #int convierte texto en numero, es decir sin decimales
# 5. Preguntaral usuario "¿A qué edad te vas a retirar?"
print("A que edad te quieres retirar?")
# 6. Definir edad_de retiro = entrada del usuario
edad_de_retiro = int(input())
# 7. Hacer años_para retiro = edad_de_retiro - edad_actual
anios_para_retiro = edad_de_retiro - edad_actual
# 8. Hacer año_de_retiro = año_actual + año_para_retiro
anio_de_retiro = anio_actual + anios_para_retiro
# 9. Mostrar mensaje "Tienes " años_para_retiro "para tu retiro"
print("Te faltan ", anios_para_retiro, "años hasta que te puedas retirar")
# 10. Mostrar mensaje "Es el año " año_actual "entonces tu retiro será el año " año_de_retiro
print("Es el año ", anio_actual, "Entonces, te podrás retirar en ", anio_de_retiro)
