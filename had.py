def nakresli_mapu(souradnice, sirka, delka):
    '''Vytvoří mapu.'''
    for j in range(delka):
        for i in range(sirka):
            if (i, j) in souradnice:
                print('X', end=' ')
            else:
                print('.', end=' ')
        print()

def pohyb(souradnice, strana):
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
    # else:
    #     print('Nemůžeš se posunout, zadej světovou stranu!')

    souradnice.append(posun)
    del souradnice[0]

souradnice = [(0,0), (1,0), (2,0)]
#nakresli_mapu(souradnice,10,4 )
def had():
    while True:
        strana = input('Zadej světovou stranu (z, j, s, v): ')
        pohyb(souradnice, strana)
        #print(souradnice)
        nakresli_mapu(souradnice, 10, 10)

had()
