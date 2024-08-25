import random


def juego_adivinanza():
    # generar un número del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinidado = False

    # Bienvenida
    print("Bienvenido al juego de adivinanza")
    print("Debes adivinar el numero entre el 1 al 100")
    print("¡Intenta adivinarlo!")

    while not adivinidado:
        # selecionar un numero entre el 1 al 100
        adivinanza = input("Introduzca un número del 1 al 100: ")

        # verficar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza} ")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicidades has ganado! el número {adivinanza} es el secreto y lo has logrado en {intentos} intentos. "
                )
        else:
            print("por favor introduzca un número valido entre el 1 al 100")


juego_adivinanza()
