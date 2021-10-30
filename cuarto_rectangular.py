# Este programa calcula el área de un cuarto rectangular y muestra el resultado en el sistema métrico (metros cuadrados) y en sistema imperial (pies cuadrados)
# 1. Inicio
# 2. Definir ancho, largo, area_metros, area_pies, factor_conversion
# 3. Hacer factor_conversion = 10.764
factor_conversion = 10.764
#4. Imprimir "Cual es el largo del cuarto en metros?"
print("Cual es el largo del cuarto en metros?")
# 5. Hacer largo = entrada del usuario
largo = float(input()) # convertir a numero
# 6. Imprimir "Cual es el ancho del cuarto en metros?"
print("Cual es el ancho del cuarto en metros?")
# 7. Hacer ancho = entrada del usuario
ancho = float(input())
# 8. Hacer area_metros = largo * ancho
area_metros = largo * ancho
# 9. Hacer area_pies = factor_conversion * area_metros
area_pies = factor_conversion * area_metros
# 10. Imprimir "Acabas de ingresar las sigientes dimensiones: ", ancho, "x", largo, "metros."
print("Acabas de ingresar las siguientes dimensiones: ", ancho, "x", largo, "metros")
# 11. Imprimir "El área es de: "
print("El área del cuarto es de: ")
# 12. Imprimir area_metros, "metros cuadrados."
print(area_metros, "metros cuadrados, y")
# 13. Imprimir area_pies "pies cuadrados."
print(area_pies, "pies cuadrados")
# 14. Fin