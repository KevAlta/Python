import random

def tirar_dado():
    return random.randint(1, 8)


def juego_de_casino():
    saldo_inicial = 10000  
    while saldo_inicial > 0:
        print(f"Tu saldo actual es: ${saldo_inicial}")
        
        
        apuesta = int(input("Haz tu apuesta (0 para salir): "))
        
        if apuesta == 0:
            break  
        
        
        if apuesta > saldo_inicial:
            print("No tienes suficiente saldo.")
            continue
        
        
        numero_elegido = int(input("Elige un número para apostar (1-12): "))
        
        if numero_elegido < 1 or numero_elegido > 12:
            print("Número no válido. Debes elegir un número entre 1 y 12.")
            continue
        
        dado1 = tirar_dado()
        dado2 = tirar_dado()
        suma_dados = dado1 + dado2
        
        print(f"Los dados muestran: {dado1} y {dado2}")
        
        
        if suma_dados == numero_elegido:
            saldo_inicial += apuesta
            print(f"Felicidades, ganaste ${apuesta}!")
        else:
            saldo_inicial -= apuesta
            print(f"Lo siento, perdiste ${apuesta}.")
    
    print("Gracias por jugar. ¡Hasta luego!")

juego_de_casino()
