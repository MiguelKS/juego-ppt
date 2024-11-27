jugador1 = input("hola jugador 1 que eliges? piedra, papel o tijeras?: ")
jugador2 = input("hola jugador 2 que eliges? piedra, papel o tijeras?: ")

if jugador1 == jugador2:
    print("!ha sido un empate!")
elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijeras" and jugador2 == "papel"):
    print("Ha ganado el jugador 1")
else:
    print("ha ganado el jugador 2")







