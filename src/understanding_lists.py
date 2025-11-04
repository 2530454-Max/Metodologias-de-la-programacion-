# Lists

"""
    Las listas nos permiten almacenar informacion en un lugar,
    la cantidad que tenga: ya sean pocos elemntos o millones de 
    elementos

    Se recomienda nombrar una variable de tipo lista en plural.

    En python ls corchetes [] definen una lista, sus elementos van separados por comas.

    Ejemplo:

"""

bicycles= ['trek', 'canondale', 'redline', 'specialized', 'giant']
print (bicycles) 

print (bicycles[0].title())

#Los indicadores comienzan en 0 y termina en n-1, donde n es el numero de elementos

print (bicycles[4].title())

#Accediendo al ultimo elemento
print (bicycles[-1].title())#Ultimo elemento
print (bicycles[-2].title())
print (bicycles[-5].title())#primer elemento

message = "Mi primer bicicleta fue una " + bicycles[4].title()+ "."
print (message)

message_f = f"Mi primer bicicleta fue una {bicycles[4].title()}."
print(message_f)

##Agregar elementos a una lista
print("")

