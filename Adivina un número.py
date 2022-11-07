import random
numero = random.randint(0,99)
intentos = 0

print("Adivina un número.")  #primer mensaje, cabecera del juego.
juego = True

while juego:
    intentos += 1
    if intentos <= 10:
        eleccion= input("Introduce un número entre 0 y 99: ")
        
        if eleccion.isdigit():
            
                try:
                    intentos = int(intentos)
                except:
                    print ("Escribe un numero entero.")
                    
                    if eleccion == numero:
                        print("Has acertado, lo has adivinado en", intentos, "intentos.")
                        juego = False
                        
                    elif eleccion > numero:
                        print("Demasiado alto, llevas", intentos, "intentos.")
                        
                    elif eleccion < numero:
                        print("Demasiado bajo, llevas", intentos, "intentos.") 
                                
    else:
        print("Has perdido, te has quedado sin intentos.")
        juego = False 

