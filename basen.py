import random
with open('basnicka.txt', encoding='utf-8') as soubor:
    obsah = soubor.read()

def prohodRadky(text):
    '''Funkce v načtené básni obrátí řádky'''
    radky = text.split('\n')
    #print(radky)
    radky.reverse()
    basen = '\n'.join(radky)
    return basen

print(prohodRadky(obsah))

def prohodSlovaRadku(text):
    '''Funkce prohodí slova v řádcích básně.'''
    radky = text.split('\n')

print(prohodSlovaRadku(obsah))
