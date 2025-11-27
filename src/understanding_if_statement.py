cars= ['audi', 'bmw', "chevrolet", "corvette", "tesla"]

for car in cars:

    if car == "bmw" or car=="tesla" or car=="audi":
        print(car.upper())
    else:
        print(car)


age = 0

try:
    age = int(input("Escribe tu edad:"))

except: 
    print("Error, ingresaste un caracter no valido")

 # <>
if age >= 18:

    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


    print("hola max")



"""
Hacer un programa que pregunte la edad de uns persona y responda lo siguiente:
    -Si la edad es menor o igual a 4, entonces la entrada es gratuita
    -Si la edad es menor a 18, pero mayor a 4, entonces la entrada cuesta 200
    -Si la edad es mayor o igual que 18, entonces la entrada cuesta $400

"""
try:
    age = int(input("Escribe tu edad:"))

except: 
    print("Error, ingresaste un caracter no valido")

if age <= 4:
    print("La esntrada es gratis ")
elif age <18 and age >4 :
    print("La entrada cuesta $200")
elif age >= 18: 
    print("La entrada cuesta $400")
