pismena = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
prepis = [1, 5, 10, 50, 100, 500, 1000]
#kombinace = pismena, prepis
#print(kombinace)

def kontrolaVstupu(seznam, vstup):
  '''
  Vstup a kontrola, zda je římské číslo + převedení na velká písmena.
  '''
  for prvek in vstup:
    if prvek not in seznam:
        print('Toto není římské písmeno! S tím ti nepomohu.')
        return None
  return vstup

def prirazeni(pismena, prepis, rimske):
  seznamCisel = []
  for prvek in rimske:
    umisteni = pismena.index(prvek)
    prirazeni = prepis[umisteni]
    seznamCisel.append(prirazeni)
  return seznamCisel

# Pro zápis dalších přirozených čísel platí tato pravidla:

# čísla zapsaná stejnými znaky vedle sebe se sčítají
# jestliže je znak menšího čísla napsán za znakem většího čísla, pak se obě tato čísla sčítají
# je-li znak většího čísla napsán za znakem menšího čísla, pak od většího se odečítá menší číslo
# znaky I, X, C se mohou opakovat nejvýše třikrát; znaky V, L, D se v každém čísle vyskytují nejvýše jednou; znak M se může opakovat libovolněkrát

def vypocet(seznam):
  cislo = 0
  for i in range(len(seznam)-1):
    cislo = cislo1
    cislo1 = int(seznam[i])
    cislo2 = int(seznam[i+1])
    if cislo1 < cislo2:
      cislo =
    for j in range (1, len(seznam)):
      cislo2 = int(seznam[j])
      if cislo1 < cislo2:
        cislo1 = cislo1 - cislo2
        break
      else:
        cislo1 = cislo1 + cislo2
        break
      break
  print(cislo1)
  return cislo



def prevod():
    '''Převede římskou číslici na arabskou. (snad)
    '''
    rimske = list(input('Zadej římskou číslici: ').upper())
    if kontrolaVstupu(pismena, rimske) != None:
      cisla = prirazeni(pismena, prepis, rimske)
      print(cisla)
      cislo = vypocet(cisla)
      #print(cislo)



    #print(rimske)



prevod()


#vstup
#kontrola, zda je římská, pokud ne - konec
#pak nějak přidat do seznamu
#porovnávání a na jeho základě sčítání a odčítání
