### FUNCIONES
# Las funciones son bloques de código reutilizables que realizan una tarea específica.
# Cuando queremis realizar la tarea que se ha definido en la función, simplemente llamamos a la función por su nombre.
"""
    Sintaxis de una funcion

    def nombre_funcion()
        acciones


        
        
        Ejemplos: Vamos a definir una que de un saludo a Christopher
"""
def greetting_Christopher():
    """
    Funcion para saldar a Christopher
    """
    for i in range(0,5):
        print("Hello Christopher")

greetting_Christopher()


#Ejemplo de una funcion que genere el nombre completo de una persona y lo regrese
def create_full_name(first_name, last_name, middle_name=""):
    full_name = f"{first_name.strip()} {middle_name} {last_name.strip()}". title()
    return full_name

firts_name = input("Ingresa tu primer nombre: ")
middle_name = input("Ingresa tu segundo nombre: (Si no tiene segundo nombre dale a enter)")
last_name = input("Ingresa tu apellido: ")
generated_full_name = create_full_name(firts_name.lower(), last_name.lower(), middle_name.lower())


print(generated_full_name)
