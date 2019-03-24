#odpovídající si seznamy základních arabských a římských číslic
pismena = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
prepis = [1, 5, 10, 50, 100, 500, 1000]

def kontrolaVstupu(seznam, vstup):
    '''
    Vstup a kontrola, zda je zadaná číslice římská.
    '''
    for prvek in vstup:
        if prvek not in seznam:
            print('Toto není římské písmeno! S tím ti nepomohu.')
            return None
    return vstup

def prirazeni(pismena, prepis, rimske):
    '''
    Funkce vloží do nového pole hodnoty jednotlivých zadaných římských číslic.
    '''
    seznamCisel = []
    for prvek in rimske:
        umisteni = pismena.index(prvek) #jaké pořadí má písmeno v seznamu pismena
        prirazeni = prepis[umisteni] #přiřazení z arabských číslic podle pořadí
        seznamCisel.append(prirazeni)
    return seznamCisel

def vypocet(seznam):
    '''
    Funkce prochází seznam s hodnotami a sčítá popř. odčítá je pro výsledek.
    '''
    arabske = seznam[0]
    for i in range(len(seznam)-1):
        dvojice = [seznam[i], seznam[i+1]]
        if dvojice[0] >= dvojice[1]:
            arabske = arabske + dvojice[1]
        else:
            arabske = arabske - 2*dvojice[0] + dvojice[1] #kombo výpočet podle papíru
    return arabske

def prevod():
    '''
    Zeptá se uživatele na římskou číslici a vypíše ji arabskou.
    '''
    rimske = list(input('Zadej římskou číslici: ').upper())
    if kontrolaVstupu(pismena, rimske) != None:
        cisla = prirazeni(pismena, prepis, rimske)
        cislo = vypocet(cisla)
        print(cislo)

prevod()
