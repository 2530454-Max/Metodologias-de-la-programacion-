#Utilizando varias listas

guisos_disponibles = ["salsa verde", "deshebrada", "mole"]
guisos_a_ordenar = ["deshebrada", "caldo de iguana"]

print("¿Que guiso desea ordenar?")
for guiso in guisos_a_ordenar:
    print(f"deseo ordenar")
    if guiso in guisos_disponibles:
        print(f"si tenemos {guiso}")
        else:
            print("No tenemos de ese guiso")
print("Realizando pedido...")

