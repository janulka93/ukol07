souradnice = [(0,0), (1,0), (2,0)] #počáteční souřadnice hada

def nakresli_mapu(souradnice, sirka, delka):
    '''Vytvoří mapu.'''
    for j in range(delka):
        for i in range(sirka):
            if (i, j) in souradnice:
                print('X', end=' ')
            else:
                print('.', end=' ')
        print()

def pohyb(souradnice, strana, delka, sirka):
    '''
    Funkce posouvá body dle zadané světové strany.
    '''
    i, j = souradnice[-1]
    posun = (i, j)
    if strana == 'v':
        posun = (i + 1, j)
    elif strana == 'j':
        posun = (i, j + 1)
    elif strana == 'z':
        posun = (i - 1, j)
    elif strana == 's':
        posun = (i, j - 1)
    if posun in souradnice:
        print('Máme tady sebevražedného hada! \nGame Over!')
        return False
    elif i not in range(0, sirka-1) or j not in range(0, delka-1):
        print('Neprojdeš dál! \nGame Over!')
        return False
    else:
        souradnice.append(posun)
        del souradnice[0]

def had():
    '''
    Hra had.
    '''
    delka = int(input('Zadej délku hracího pole: '))
    sirka = int(input('Zadej šířku hracího pole: '))
    nakresli_mapu(souradnice, delka, sirka)
    while True:
        strana = input('Zadej světovou stranu (z, j, s, v): ')
        if pohyb(souradnice, strana, sirka, delka) != False:
            nakresli_mapu(souradnice, delka, sirka)
        else:
            break
had()
