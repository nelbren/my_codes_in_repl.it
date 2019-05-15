#!/usr/bin/python3
# ahorcado_v01.py - 2019-05-13 - nelbren.com - first try
import random
palabras = ["apple", "banana", "cherry"]
random.shuffle(palabras)
letras = []
intentos = 7
letra_ingresada = ''
while True:
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
    if palabra_encontrada:
        print('En hora buena.')
        break
    if not letra_encontrada:
        intentos = intentos - 1
        print('Intentos restantes', intentos)
    if intentos == 0:
        print('Ahorcado!\nLa palabra era:', palabras[0])
        break
    letra_ingresada = input('Letra: ')

