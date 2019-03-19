zvirata = ['pes', 'kočka', 'králík', 'had']
for slovo in zvirata:
    print(slovo)

def podPetPism(seznam):
    '''Funkce vrací jména ze seznamu, která jsou kratší než X písmen.
    '''
    pocet = int(input('Zadej horní hranici počtu písmen ve slově: '))
    vysledek = []
    for slovo in seznam:
        if len(slovo) < pocet:
            vysledek.append(slovo)
    return vysledek

#pro ověření
print(podPetPism(zvirata))

def zacinaNa(seznam):
    '''Funkce vrací slova ze seznamu, jež začínají na zadané písmeno.
    '''
    pismeno = input('Zadej písmeno, na které mají slova ze seznamu začínat: ')
    vysledek = []
    for slovo in seznam:
        if slovo[0] == pismeno.lower():
            vysledek.append(slovo)
        else:
            break
    if vysledek:
        return vysledek
    else:
        print('V seznamu se nevyskytuje žádné slovo začínající na písmeno:', pismeno.capitalize())

#pro ověření
print(zacinaNa(zvirata))

def jeVSeznamu(seznam):
    '''Funkce zjistí, zda je zadané slovo v seznamu zvířat.
    '''
    zvire = input('Je toto zvíře v seznamu? ')
    return zvire in seznam

print(jeVSeznamu(zvirata))

def triSeznamy(seznamA, seznamB):
    '''Funkce dostane dva seznamy a vrátí tři.
        - prvky v obou seznamech (sjednocení)
        - prvky jen v prvním seznamu (rozdíl)
        - prvky jen v druhém seznamu (rozdíl)
    '''
    vysledekS = seznamA + seznamB
    for prvek in vysledekS:
#prvky se mohou po použití + opakovat → kontrola počtu výskytu a případné odstranění
        if vysledekS.count(prvek) > 1:
            vysledekS.remove(prvek)

    vysledekR1 = []
    for prvek in seznamA:
        if prvek not in seznamB:
            vysledekR1.append(prvek)

    vysledekR2 = []
    for prvek in seznamB:
        if prvek not in seznamA:
            vysledekR2.append(prvek)

    return vysledekS, vysledekR1, vysledekR2

print(triSeznamy(['kun', 'pes', 'ptak', 'liska'],['kun', 'kocka', 'vrabec', 'ptak']))
