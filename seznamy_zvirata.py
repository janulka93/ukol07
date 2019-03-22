zvirata = ['pes', 'kočka', 'králík', 'had']
# for slovo in zvirata:
#     print(slovo)

def podPetPism(seznam):
    '''Funkce vrací jména ze seznamu, která jsou kratší než X písmen.
    '''
    odpoved = input('Zadej horní hranici počtu písmen ve slově: ')
    try:
        pocet = int(odpoved)
    except ValueError:
        print('Tohle není číslo. Defaultně nastavuji pětku!')
        pocet = 5
    vysledek = []
    for slovo in seznam:
        if len(slovo) <= pocet:
            vysledek.append(slovo)
    return vysledek

#pro ověření
print(podPetPism(zvirata))

def zacinaNa(seznam):
    '''Funkce vrací slova ze seznamu, jež začínají na zadané písmeno.
    '''
    pismeno = input('Zadej písmeno, na které mají slova ze seznamu začínat: ')
    vysledek = []
    if len(pismeno) == 1 :
        for slovo in seznam:
            if slovo[0] == pismeno.lower():
                vysledek.append(slovo)
        if vysledek:
            print('Zvířata v seznamu na písmeno', pismeno, 'jsou:', vysledek)
        else:
            print('V seznamu se nevyskytuje žádné slovo začínající na písmeno:', pismeno.capitalize())
    else:
        print('Toto není jedno písmeno! Nic se nedozvíš.')
#pro ověření
zacinaNa(zvirata)

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

    print('sjednocení dvou seznamů:', vysledekS)
    print('rozdíl první - druhá:', vysledekR1)
    print('rozdíl druhá - první:', vysledekR2)

zvirata2 =  ['kun', 'pes', 'ptak', 'kočka']
triSeznamy(zvirata, zvirata2)

def serad(seznam):
    '''Funkce seřadí prvky daného seznamu podle abecedy.
    '''
    seznam.sort()
    return seznam

print('Zvířata seřazená podle abecedy:', serad(zvirata))

zvirata.append('andulka')

def seradKlicem(seznam):
    '''Seřadí seznam podle klíče'''
    seznamKlic = []
    vysledek = []
    for prvek in seznam:
        ntice = [prvek[1:], prvek]
        seznamKlic.append(ntice)
    seznamKlic.sort()
    for prvek in seznamKlic:
        vysledek.append(prvek[1]) #print(seznamKlic)
    return vysledek


print(seradKlicem(zvirata))
