import mysql.connector
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Conexión a la base de datos
cnx = mysql.connector.connect(user='root', password='12345',
                              host='localhost', database='juego_clue')
cursor = cnx.cursor()

# Consulta para obtener los nombres de sospechosos
cursor.execute('SELECT sospechosos FROM datos')
sospechosos = [row[0] for row in cursor.fetchall()]

# Consulta para obtener los nombres de habitaciones
cursor.execute('SELECT habitaciones FROM datos')
habitaciones = [row[0] for row in cursor.fetchall()]

# Consulta para obtener los nombres de armas
cursor.execute('SELECT armas FROM datos')
armas = [row[0] for row in cursor.fetchall()]

# Obtener elementos aleatorios
victima_aleatorio = random.choice(sospechosos)
sospechoso_aleatorio = random.choice([s for s in sospechosos if s != victima_aleatorio])
habitacion_aleatoria = random.choice(habitaciones)
arma_aleatoria = random.choice(armas)

#Premisas
Premisa = f'Han matado a {victima_aleatorio}, tu trabajo sera descubrir quien fue, en donde y con que arma, mucha suerte!'

#Cartas fuera del sobre
no_sospechoso = random.choice([s for s in sospechosos if s != sospechoso_aleatorio])
no_arma = random.choice([s for s in armas if s != arma_aleatoria])
no_habitacion = random.choice([s for s in habitaciones if s != habitacion_aleatoria])
carta_pista = (no_sospechoso, no_arma, no_habitacion)


#Mis cartas
cartas_sospechoso = random.choice([s for s in sospechosos if s != no_sospechoso])
cartas_armas = random.choice([s for s in armas if s != no_arma])
cartas_habitacion = random.choice([s for s in habitaciones if s !=no_habitacion])
cartas_mias = (cartas_sospechoso, cartas_armas, cartas_habitacion)

#No son sospechosos
no_sospechoso1 = random.choice([s for s in sospechosos if s != sospechoso_aleatorio])
no_sospechoso2 = random.choice([s for s in sospechosos if s != sospechoso_aleatorio and s != no_sospechoso1])
no_sospechoso3 = random.choice([s for s in sospechosos if s != sospechoso_aleatorio and s != no_sospechoso1 and s != no_sospechoso2])
no_sospechoso4 = no_sospechoso

#Armas no usadas
no_arma1 = random.choice([s for s in armas if s != arma_aleatoria])
no_arma2 = random.choice([s for s in armas if s != arma_aleatoria and s != no_arma1])
no_arma3 = random.choice([s for s in armas if s != arma_aleatoria and s != no_arma1 and s != no_arma2])
no_arma4 = cartas_armas

#Lugares que no son escenas del crimen
no_habitacion1 = random.choice([s for s in habitaciones if s != habitacion_aleatoria])
no_habitacion2 = random.choice([s for s in habitaciones if s != habitacion_aleatoria and s != no_habitacion1])
no_habitacion3 = random.choice([s for s in habitaciones if s != habitacion_aleatoria and s != no_habitacion1 and s != no_habitacion2])
no_habitacion4 = cartas_habitacion

#Solucion
Solucion1 = f'En el/la {habitacion_aleatoria}, {sospechoso_aleatorio} mata a {victima_aleatorio} con un(a/as) {arma_aleatoria} despues de una discusion por dinero.'
Solucion2 = f'En el/la {habitacion_aleatoria}, {sospechoso_aleatorio} mata a {victima_aleatorio} con un(a/as) {arma_aleatoria} en un acto de defensa propia despues de que el/ella la atacara.'
Solucion3 = f'En el/la {habitacion_aleatoria}, {sospechoso_aleatorio} mata a {victima_aleatorio} con un(a/as) {arma_aleatoria} durante una pelea por celos.'
Solucion4 = f'En el/la {habitacion_aleatoria}, {sospechoso_aleatorio} mata a {victima_aleatorio} con un(a/as) {arma_aleatoria} despues de descubrir que le habia borrado su perfil de OCC.'
Solucion5 = f'En el/la {habitacion_aleatoria}, {sospechoso_aleatorio} mata a {victima_aleatorio} con un(a/as) {arma_aleatoria} porque le estrello su coche'
Soluciones = (Solucion1, Solucion2, Solucion3, Solucion4, Solucion5)
Solucion_aleatoria = random.choice(Soluciones)

# Consulta para obtener los nombres de sospechosos excluyendo a la víctima
cursor.execute('SELECT sospechosos FROM datos WHERE sospechosos != %s', (victima_aleatorio,))
sospechosos = [row[0] for row in cursor.fetchall()]

#Presentación
print('\nBienvenido al juego de clue\n')

# Iniciar el juego
while True:
    #Premisa 
    print(f'{Premisa}\n')
    print(f'Tus cartas son:{cartas_mias}')
    # Preguntar al jugador qué información desea obtener
    print("Que informacion deseas obtener? Selecciona una opcion: \n")
    print("1. Informacion acerca de los sospechosos")
    print("2. Informacion acerca de las habitaciones")
    print("3. Informacion acerca de las armas")
    print("4. Hacer una suposicion acerca de la solucion")
    print("5. Ver 3 cartas que no estan en el sobre")
    print("6. Informacion 1")
    print("7. Informacion 2")
    print("8. Informacion 3")
    print("9. Informacion 4")
    print("10. Ver solucion")
    print("11. Salir del juego")
 
    opcion = input("> ")

        # Proporcionar información acerca de los sospechosos
    if opcion == "1":
        print("\nLos sospechosos son:")
        for sospechoso in sospechosos:
            print("- " + sospechoso)

    # Proporcionar información acerca de las habitaciones
    elif opcion == "2":
        print("\nLas habitaciones son:")
        for habitacion in habitaciones:
            print("- " + habitacion)

    # Proporcionar información acerca de las armas
    elif opcion == "3":
        print("\nLas armas son:")
        for arma in armas:
            print("- " + arma)

    elif opcion == "4":
        print("\nHaga su suposicion en el siguiente formato: 'sospechoso', 'habitacion', 'arma'")
        suposicion = input("> ")
        if suposicion == f"{sospechoso_aleatorio}, {habitacion_aleatoria}, {arma_aleatoria}":
            print("Felicitaciones, has resuelto el caso!")
            break
        else:
            print("\n***Lo siento, esa no es la solucion correcta.***\n")
            

    elif opcion == "5":
        print(f"\nTres cartas que no estan en el sobre son: {carta_pista}")

    elif opcion == "6":
        print(f"{no_sospechoso1} estuvo toda la noche con {no_sospechoso2} en {no_habitacion1}, dicen haber visto que alguien se llevo {no_arma1}, pero no saben a donde")

    elif opcion == "7":
        print(f"{no_sospechoso3} vio que alguien llevaba muchas cosas, pero no sabe exactamente que y que estuvo dando vueltas entre {habitacion_aleatoria} y {no_habitacion3}")

    elif opcion == "8":
        print(f"{no_sospechoso4} estuvo solo en la noche, pero porque se sentia enfermo, por lo cual se la paso en {no_habitacion2}")

    elif opcion == "9":
        print(f"{no_habitacion4} estuvo cerrada casi toda la noche, porque estaba sucia/o dice {no_sospechoso4}")

    elif opcion == "10":
        print(f"La solucion es: {Solucion_aleatoria}")

    elif opcion == "11":
        break

# Cerrar la conexión a la base de datos
cnx.close()
