


# Zdravím všechny a přeji krásný páteční den, který strávíme s hadem.
# Mám dotaz potřebovala bych asi trošku vysvětlit jak to funguje s těmi souřadnicemi.
# Mám vykreslenou mapu teček (postup stejný jako na přednášce s mapou na násobilku)
# ale furt mi nejde do hlavy ja mám zadat že podle souřadnic má být x nebo 2.

# Tereza Balonova   [1 day ago]
# Myslíš x nebo tečka? No pokud to mas podle násobilky, tak já jsem do
# jednoho místa v kódu přidala podmínku  if (x, y) in souřadnice: vykreslí křížek,
# else tečku. (edited)
#
# Tereza Balonova   [1 day ago]
# přičemž x,y je v te nasobilce a, b, abych to uvedla na pravou miru
#
# Lumír Balhar   [1 day ago]
# Přesně tak. Mapa vlastně znamená jen vykreslení teček tam, kde nemá být
# nic jiného (had, jídlo).



def nakresli_mapu(souradnice, velikost):
    '''Vytvoří mapu.'''
    radky = []
    for j in range(velikost):
        radek = []
        for i in range(velikost):
            if (i, j) in souradnice:
                radek.append('X')
            else:
                radek.append('.')
        radky.append(radek)

    return radky

pole = nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)], 10)
print(pole)

def pohyb(souradnice, strana):
    '''
    Funkce posouvá body dle zadané světové strany.
    '''
    i, j = souradnice[0]
    posun = (i, j)
    if strana == 'v':
        posun = (i + 1, j)
    elif strana == 'j':
        posun = (i, j + 1)
    elif strana == 'z':
        posun = (i - 1, j)
    elif strana == 's':
        posun = (i, j - 1)
    souradnice.append(posun)

souradnice = [(0,0)]
pohyb(souradnice,'v')
print(souradnice)
