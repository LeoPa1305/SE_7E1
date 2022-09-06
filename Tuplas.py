tupla = ('Uno','Dos','Tres','Cuatro','Cinco')
lista = ['Seis', 'Siete', 'Ocho', 'Nueve', 'Diez']

print(tupla)
print(tupla[2]) #Imprimimos el elemento en la ubicación 2 de la tupla

print(type(lista))
print(type(tupla))

tupla1 = tuple(lista)
lista1 = list(tupla)

print(type(lista1))
print(type(tupla1))
