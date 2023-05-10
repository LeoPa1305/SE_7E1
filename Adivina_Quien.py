import mysql.connector

# Conexión a la base de datos
cnx = mysql.connector.connect(user='root', password='12345',
                              host='localhost', database='Manchester_ceti')
cursor = cnx.cursor()

# Pedirle al usuario que piense en un jugador
print("\n*****************************\n")
print("Piensa en un jugador\n")

# Hacer seis preguntas sobre el jugador
partidos = input("Jugo todos los partidos? (s/n): ")
gol = input("Metio gol? (s/n): ")
estudia = input("Estudia en el ceti? (s/n): ")
pofc = input("Es Portero o Defensa? (s/n): ")
mcdc = input("Es Medio o Delantero? (s/n): ")
opcion_6 = input("Su numero de playera esta entre el 5 y el 20? (s/n): ")

# Armar la consulta SQL basada en las respuestas del usuario
consulta = f"SELECT nombre FROM jugadores WHERE Partidos = {partidos == 's'} AND Gol = {gol == 's'} AND Estudia_ceti = {estudia == 's'} AND PO_DFC = {pofc == 's'} AND MC_DC = {mcdc == 's'} AND OPCION_6 = {opcion_6 == 's'};"
# Ejecutar la consulta y obtener el resultado
cursor.execute(consulta)
resultado = cursor.fetchone()

# Mostrar el resultado
if resultado:
    print(f"Adivine que estas pensando en {resultado[0]}")
else:
    print("No pude adivinar en quien estas pensando")
    
# Cerrar la conexión a la base de datos
cursor.close()
cnx.close()