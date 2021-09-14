# Juego: Concurso de Preguntas y Respuestas
El programa está desarrolado en Python 3.9.7

El juego consiste en responder a las preguntas de opción múltiple con única respuesta generadas aleatoriamente, dependiendo del nivel del juego en el cual se encuentra el jugador. Cada pregunta tiene cuatro opciones de respuesta, de las cuales sólo una es la correcta. El juego consta de cinco niveles y cada nivel tiene cinco preguntas con una complejidad mayor a medida que se avanza en el juego, otorgando premios. Si el usuario gana pasa a la siguiente ronda (nivel), si pierde se finaliza el juego.

El usuario tiene la posibilidad de continuar o retirarse del juego en cualquier momento que lo desee, antes de continuar con la siguiente pregunta; si decide retirarse del juego, pasa los cinco niveles o digita una opción incorrecta, el programa exporta los datos del jugador (nombre, última pregunta contestada, respuesta del jugador, respuesta correcta, nivel y premio acumulado)  a un archivo (diccionario) con extensión txt con nombre "informacionDelJugador" y lo guarda en la ruta especificada (especificar la ruta en la función exportarInformacionJugador()). 
