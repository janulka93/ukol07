pismena = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
prepis = [1, 5, 10, 50, 100, 500, 1000]
#kombinace = pismena, prepis
#print(kombinace)

def kontrolaVstupu(seznam, vstup):
    '''
    Vstup a kontrola, zda je římské číslo.'''
    for prvek in vstup:
        if prvek not in seznam:
            print('Toto není římské písmeno! S tím ti nepomohu.')
            return None
        # if 'vv'.lower() or 'll'.lower() or 'dd'.lower() in seznam:
        #     print('Toto není římské písmeno! S tím ti nepomohu.')
        #     return None
    return vstup

def prirazeni(pismena, prepis, rimske):
    seznamCisel = []
    for prvek in rimske:
        umisteni = pismena.index(prvek)
        prirazeni = prepis[umisteni]
        seznamCisel.append(prirazeni)
    print(seznamCisel)
    return seznamCisel

# Pro zápis dalších přirozených čísel platí tato pravidla:

# čísla zapsaná stejnými znaky vedle sebe se sčítají
# jestliže je znak menšího čísla napsán za znakem většího čísla, pak se obě tato čísla sčítají
# je-li znak většího čísla napsán za znakem menšího čísla, pak od většího se odečítá menší číslo
# znaky I, X, C se mohou opakovat nejvýše třikrát; znaky V, L, D se v každém čísle vyskytují nejvýše jednou; znak M se může opakovat libovolněkrát

def vypocet(seznam):
    arabske = seznam[0]
    for i in range(len(seznam)-1):
        dvojice = [seznam[i], seznam[i+1]]
        if dvojice[0] >= dvojice[1]:
            arabske = arabske + dvojice[1]
        else:
            arabske = arabske - dvojice[0]
    return arabske

def prevod():
    '''Převede římskou číslici na arabskou. (snad)
    '''
    rimske = list(input('Zadej římskou číslici: ').upper())
    if kontrolaVstupu(pismena, rimske) != None:
        cisla = prirazeni(pismena, prepis, rimske)
        print(cisla)
        cislo = vypocet(cisla)
        print(cislo)

prevod()


#vstup
#kontrola, zda je římská, pokud ne - konec
#pak nějak přidat do seznamu
#porovnávání a na jeho základě sčítání a odčítání
