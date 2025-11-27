"""
    vamos a realizar un programa que defina
"""
CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
attempt = 0
remaining_attempt = MAX_ATTEMPTS
while attempt < MAX_ATTEMPTS:
    user_input = input("Ingresa tu PIN: ")
    if user_input == CORRECT_PIN:
        print("Le atinaste, acceso concedido")
    else: 
        attempt +=1
        remaining_attemps = MAX_ATTEMPTS - attempt
    if remaining_attemps > 0:
        print("Ingresaste un pin no valido")
        print(f"Te quedan {remaining_attemps} intentos")
    else: 
        print("cuenta bloqueada, dejate de mermas.")
        
