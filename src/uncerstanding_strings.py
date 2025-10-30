"""
String variables

Un string es de manera sencilla una serie de caracteres. En python , todo lo que se encuentre
dentro de comillas simples (' ')o dobles (" ") sera considerado un string.

Ejemplos:
"Esto es un string"
'Esto tambien es un string'

'Le dije a un amigo que python era mi lenguaje favorito'
" El lenguaje 'Python' lleva el nombre por Monty Python, no por la serpiente "

"""
name = "clase de programacion"
print(name)

# title
print (name.title())
"""
Un metodo es una accion que python puede realizar en un fragmento de datos o sobre una variable

El punto . despyues de una vriable seguidp del metodo title() dice que se tiene que ejecutar el metodo title de la variable

Todos los metodos van seguidos de parentesis
porque en ocasiones necesitan informacion adicional
para funcionar, la cual iria dentro de los parentesis.

en esta ocasion el metodo .title() no requiere informacion adicional para funcionar
"""

print("metodo upper:",name.upper())
print("Metodo lower:",name.lower())

# Concatenion strings
first_name= "max"
last_name= "hernandez"
full_name = first_name +" "+ last_name
print(full_name)
print(full_name.title())

#whitespaces

"""
Un whitespace se refiere a cualquier caracter que no se imprime, es decir , un espacio, tabulador
Los whitespacesse utilizan comunmente para organizar las salidas.

Ejemplos:
-Tabulador: \t
-Salto de linea: \n
"""

print("Whitespaces Tabulador")
print("python")
print("\tpython")
print("\t\tpython")

print("Whitespace salto de linea")
print("Languages: \n\tPython\nC\n\tJavascript")



#Eliminacion de espacios en blanco

programming_languages = " Python "
print(programming_languages)
print(programming_languages.rstrip())
print(programming_languages.lstrip())
print(programming_languages.strip())
