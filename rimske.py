pismena = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
prepis = [1, 5, 10, 50, 100, 500, 1000]
kombinace = pismena, prepis
print(kombinace)
rimske = list(input('Zadej římskou číslici: ').upper())
for prvek in rimske:
    if prvek not in pismena:
        print('Toto není římské písmeno! S tím ti nepomohu.')
        break

seznamCisel = []
for prvek in rimske:
    umisteni = pismena.index(prvek)
    prirazeni = prepis[umisteni]
    seznamCisel.append(prirazeni)
print(seznamCisel)

cislo = 0
novy_seznam = []
for prvek in seznamCisel:
    cislo = prvek
    if prvek >= cislo:
        znamenko = '+'
        novy_seznam.append(prvek)
        novy_seznam.append(znamenko)

        cislo = prvek
    else:
        znamenko = '-'
        novy_seznam.append(prvek)
        novy_seznam.append(znamenko)

        cislo = prvek
print(novy_seznam)






def prevod(rimske):
    '''Převede římskou číslici na arabskou. (snad)
    '''
#vstup
#kontrola, zda je římská, pokud ne - konec
#pak nějak přidat do seznamu
#porovnávání a na jeho základě sčítání a odčítání
