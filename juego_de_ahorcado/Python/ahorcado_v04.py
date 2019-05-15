#!/usr/bin/python3
# ahorcado_v04.py - 2019-05-13 - nelbren.com - uso de generador de palabras aleatorias en línea
# Imagenes de ahorcado de:
# https://www.lawebdelprogramador.com/codigo/Python/5054-Juego-del-ahorcado-en-python-3.html
# Generador de Palabras Aleatorias de:
# http://www.danielpinero.com/generador-palabra-aleatoria
import re
from urllib.request import urlopen


def obtener_palabra_al_azar():
    url = "http://www.danielpinero.com/generador-palabra-aleatoria"
    html = urlopen(url).read().decode('utf-8')
    busqueda = re.search('<b>(.*)<\/b>', html, re.IGNORECASE)
    if busqueda:
        palabra = busqueda.group(1)
    else:
        palabra = 'fracaso'
    return palabra


def configuracion_de_variables():
    global IMAGENES_AHORCADO, palabras, letras, intentos, letra_ingresada
    IMAGENES_AHORCADO = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
    palabras = ["apple", "banana", "cherry"]
    #random.shuffle(palabras)
    palabras[0] = obtener_palabra_al_azar()
    letras = []
    intentos = 7
    letra_ingresada = ''


def mostrar_palabra():
    global letra_encontrada, palabra_encontrada, palabras, letras
    print('Tip: Es una palabra con', len(palabras[0]), 'letras : ', end='')
    letra_encontrada = False
    palabra_encontrada = True
    for letra_palabra in palabras[0]:
        existe_en_letras = False
        if letra_palabra == letra_ingresada:
            letras.append(letra_palabra)
            letra_encontrada = True
        for letra in letras:
            if letra == letra_palabra:
                existe_en_letras = True
                break
        if existe_en_letras:
            print(letra_palabra, '', end='')
        else:
            print('_ ', end='')
            palabra_encontrada = False
    print('')


def condicion_para_salir():
    global palabra_encontrada, letra_encontrada, IMAGENES_AHORCADO, intentos
    salir = False
    if palabra_encontrada:
        print('En hora buena.')
        salir = True
    if not letra_encontrada:
        print(IMAGENES_AHORCADO[7 - intentos])
        intentos = intentos - 1
        print('Intentos restantes', intentos)
    if intentos == 0:
        print('Ahorcado!\nLa palabra era:', palabras[0])
        salir = True
    return salir


configuracion_de_variables()

while True:
    mostrar_palabra()
    if condicion_para_salir():
        break
    letra_ingresada = input('Letra: ')

