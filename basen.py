import random
with open('basnicka.txt', encoding='utf-8') as soubor:
    obsah = soubor.read()

def obratRadky(text):
    '''Funkce v načtené básni obrátí verše.'''
    radky = text.split('\n')
    #print(radky)
    radky.reverse()
    basen = '\n'.join(radky)
    return basen

print('\nNEJPRVE BÁSEŇ S OBRÁCENÝMI VERŠI: \n')
print(obratRadky(obsah))

def obratSlovaRadku(text):
    '''Funkce obrátí slova ve verších básně.'''
    radky = text.split('\n')
    for i in range(len(radky)):
        radek = radky[i].split(' ')
        radek.reverse()
        vers = ' '.join(radek).lstrip()
        print(vers)

print('\nTEĎ BÁSEŇ S OBRÁCENÝMI SLOVY VE VERŠÍCH: \n')
obratSlovaRadku(obsah)

def obratSloky(text):
    '''Funkce prohodí jednotlivé sloky básně.'''
    radky = text.split('\n\n')
    radky.reverse()
    basen = '\n\n'.join(radky)
    return basen

print('\nA BÁSEŇ S OBRÁCENÝM POŘADÍM SLOK:\n')
print(obratSloky(obsah))
