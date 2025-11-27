"""
    Un progrma que: 
    -Cuente cuantos numeros ha ingresado el usuario
    -Realice la suma de estos numeros
    -Me diga cual es el minimo de numeros ingresados
    -Me diga cual es el maximo de los numeros ingresados

"""
counter = 0
sum_numbers= 0.0
minimo = None
maximo = None

while True:
    print ("Escribe exit para salir ")
    user_input = input("Ingresa una cantidad (MXN): ")


    if user_input == 'exit':
        break
    
    try:
        value= float (user_input)
    except ValueError:
        print("Caracter invalido. Por favor ingresa un numero")
    except KeyboardInterrupt:
        print("Salida manual")
        break
    counter = counter + 1
    sum_quantitites += value

    if minimo is None or value <minimo 
        minimo = value