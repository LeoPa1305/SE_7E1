numeros = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]

print(numeros)
print(numeros[1])

print("el primer numero es:",numeros[0])

numeros.remove("diez") #Con la función remove se borra un elemento de la lista
print(numeros)

numeros.insert(9,"diez") #Se agregó el número borrado
print(numeros)


print("\n La lista contiene",len(numeros),"numeros")

