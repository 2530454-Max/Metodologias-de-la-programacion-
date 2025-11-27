#Problema 1: full name formatter
"""
Dado el nombre completo de una persona en una sola cadena (por ejemplo: "Maximiliano Hernandez Sanchez"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: M.H.S.).
"""
def format_full_name(full_name):
    # Paso 1: Normalizar el texto
    full_name = full_name.strip()  # Eliminar espacios al inicio y al final
    full_name = ' '.join(full_name.split())  # Eliminar espacios extra entre palabras
    full_name = full_name.title()  # Convertir a Title Case

    # Paso 2: Obtener las iniciales
    name_parts = full_name.split()  # Dividir el nombre en partes
    initials = '.'.join([part[0] for part in name_parts]) + '.'  # Obtener la primera letra de cada parte y unir con puntos

    return full_name, initials
# Ejemplo de uso
input_name = "  maximiliano   hernandez   sanchez  "
formatted_name, initials = format_full_name(input_name)
print(f"Nombre formateado: {formatted_name}")
print(f"Iniciales: {initials}")
# --- IGNORE ---
# contar caracteres en un nombre
nombre = "Maximiliano Hernandez Sanchez"
print(len(nombre))         # 29 (incluye los espacios)
# contar palabras
print(len(nombre.split())) # 3
# listas y diccionarios
print(len([1,2,3]))        # 3
print(len({'a':1,'b':2}))  # 2
# --- END IGNORE ---
