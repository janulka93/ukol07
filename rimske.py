pismena = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
prepis = [1, 5, 10, 50, 100, 500, 1000]
kombinace = pismena, prepis
print(kombinace)
rimske = list(input('Zadej římskou číslici: ').upper())
for prvek in rimske:
    if prvek not in pismena:
        print('Toto není římské písmeno! S tím ti nepomohu.')
        break

for prvek in rimske:
    umisteni = pismena.index(prvek)
    prirazeni = prepis[umisteni]
    print(prirazeni)
