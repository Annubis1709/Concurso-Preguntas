import random
import time
from preguntasRespuestas import preguntas, opciones

def mensajeBienvenida():
    print("\t", "*"*100)
    print("\tBIENVENIDO AL CONCURSO DE PREGUNTAS Y RESPUESTAS".center(100))
    print("\tEL juego consiste en responder las preguntas de opcion multiple (4) con una unica respuesta".center(100) )
    print("\tEl juego consta de 5 niveles, 5 preguntas por nivel".center(100))
    print("\t", "*" * 100)
    print("\t¿Desea jugar o salir del juego?")
    print("\t\t 1. Jugar")
    print("\t\t 2. Salir")
    print("\t", "*" * 100)
    try:
        respuestaDelJugador = int(input("\tDigite la opcion: "))
        if respuestaDelJugador == 1:
            pass

        elif respuestaDelJugador == 2:
            print("\tHas decidido no jugar. Hasta Pronto")
            exit(4)
        else:
            print("¡Ooops! digitaste una opcion no valida")
            print("\tSaliendo del juego")
            exit(4)
    except ValueError:
        print("¡Ooops! digitaste una opcion no valida")
        print("\tSaliendo del juego")
        exit(4)

"""
Muestra al usuario una pregunta generada aleatoriamente del diccionario de preguntas, dependiendo del nivel del juego
 en el cual se encuentra el usuario junto con las cuatro opciones de respuesta.
"""
def preguntasPorNivel(numero):
    print(preguntas[numero]["respuesta"])
    print("Pregunta: ")
    print(preguntas[numero]["pregunta"])
    for x in opciones[numero - 1]:
        print(x)


"""
Verifica si la respuesta del jugador coincide con la respuesta correcta almacenada en el diccionario de preguntas,
retorna verdadero si la respuesta es correcta y falso en caso contrario 
"""
def verificarRespuesta(numero):
    if respuesta_usuario.upper() == preguntas[numero]["respuesta"]:
        return True
    else:
        return False

"""
Asigna el premio por nivel 
"""
def premiosPorNivel(nivel):
    premios = [5000000, 10000000, 15000000, 25000000, 35000000]
    premio = premios[nivel]
    return premio

"""
Verifica si el jugador desea continuar o salir en algun punto dado del juego ( antes de realizar la pregunta del 
siguiente nivel). Si el usuario ingresa 1, continua con la pregunta del siguiente nivel, si ingresa 0 se le notifica 
 que ha dado la opcion de abandonar el juego junto con informacion del nivel en el cual quedo y cuanto se lleva de
  premio acumulado al igual si marca una opcion no valida con la excepcion que notifica que la opcion ingresada no es 
  la correcta.
"""
def verificarOpcionJugador():
    try:
        respuestaDelJugador = int(input("\tIngrese 1 para continuar o 2 para salir del juego: "))
        if respuestaDelJugador == 1:
            pass

        elif respuestaDelJugador == 2:
            print("\t", "*" * 120)
            print(f"\tHas decidido abandonar el juego. Quedaste en el nivel: {nivel + 1}, con un acumulado de premios de: "
                  f"${acumulado:,} millones.")
            print("\t", "*" * 120)
            exportarInformacionJugador()
            exit()
        else:
            print(f"\t¡Ooops! digitaste una opcion no valida, :( . Quedaste en el nivel: {nivel + 1}, con un acumulado de"
                  f" premios de: ${acumulado:,} millones.")
            exportarInformacionJugador()
            exit()
    except ValueError:
        print(f"\t¡Ooops! digitaste una opcion no valida, :( . Quedaste en el nivel: {nivel + 1}, con un acumulado de "
              f"premios de: ${acumulado:,} millones.")
        exportarInformacionJugador()
        exit()

"""
Informa al jugador cuanto ha ganado y lleva de acumulado por cada nivel del juego que supere y pregunta si desea 
continuar con el juego
"""

def mensaje(nombre_jugador):
    if nivel >= 0 and nivel <= 3:
        print("\t", "*" * 100)
        print(f"\t¡Felicidades {nombre_jugador}! pasaste el nivel: {nivel + 1}. ¡Has ganado ${premiosPorNivel(nivel):,} millones de pesos!".center(100))
        print("\t", "*" * 100)
        print(f"\tTienes un acumulado de: ${acumulado:,}. ¿Deseas continuar al siguiente nivel ({nivel + 2}) y "
              f"ganar el premio de: ${premiosPorNivel(nivel + 1):,}?")
        verificarOpcionJugador()
    else:
        print("\t", "*" * 100)
        print(f"\t¡Felicidades {nombre_jugador}, has ganado el premio mayor: ${acumulado:,}!".center(100))
        print("\t", "*" * 100)
        exportarInformacionJugador()
        exit()


"""
Genera un numero entero aleatorio entre los rangos inicial y final, dependiendo del nivel del juego en el cual se 
encuentra el usuario.
"""
def numeroAleatorio(nivel):
    inicial = 5 * nivel + 1
    final = 5 * (nivel + 1)
    return random.randint(inicial, final)

"""
Exporta los datos del jugador a un archivo txt en la ruta especificada (/home/draconis/Documentos/SOFKA/) con nombre de
archivo: informacionDelJugador.txt.
"""
def exportarInformacionJugador():
    index = respuesta_usuario.upper()
    letraValor = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3
    }
    informacionJugador = {
        "Nombre Del Jugador" : nombre_jugador,
        "Ultima pregunta contestada": preguntas[numero]["pregunta"],
        "Respuesta del Jugador" : index,
        "Respuesta Correcta" : opciones[numero][letraValor.get(index)],
        "Nivel Jugador": nivel + 1,
        "Premio Acumulado": f"${acumulado:,} millones"
    }

    ruta = '/home/draconis/Documentos/PYTHON PROJECT/RETO TECNICO/'
    #Cambiar a la ruta a la cual desea guardar el archivo
    archivo = open(r'informacionDelJugador.txt', "w")
    archivo.write(str(informacionJugador))
    print(f"\tExportando archivo con los datos del jugador a la siguiente ruta:\n {ruta}")
    time.sleep(3)





nivel = 0
acumulado = 0
ronda = 5
mensajeBienvenida()
nombre_jugador = input("\tEscriba su su nombre: ")
while ronda > 0:
    numero = numeroAleatorio(nivel)
    preguntasPorNivel(numero)
    respuesta_usuario = input("Ingrese la respuesta: ")
    if verificarRespuesta(numero):
        acumulado += premiosPorNivel(nivel)
        mensaje(nombre_jugador)
        ronda -= 1
        nivel += 1
    else:
        print(f"Respuesta incorrecta {nombre_jugador} :( , el juego ha finalizado")
        break
