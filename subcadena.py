cadena = "qqwqweqwerqwertyfghjk"

subcadena = []

primera_posicion = True
for letra in cadena:
    if primera_posicion:
        subcadena.append(cadena[0])
        primera_posicion = False
        continue
    if letra not in subcadena[-1]:
        subcadena[-1] = subcadena[-1] + letra
    else:
        subcadena.append(letra)

    primera_posicion = False

largonum = 0
largostr = ""
for cadenas in subcadena:
    if len(cadenas) > largonum:
        largonum = len(cadenas)
        largostr = cadenas

print(f'La subcadena más larga sin repetir letras es: "{largostr}"')