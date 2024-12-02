from neo4j import GraphDatabase
import random
import string

# Configuración para conectarse a la base de datos Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"
password = "entrega2"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Definir equipos con sus ciudades y ligas
equipos = [
    {"nombre": "Manchester City", "ciudad": "Manchester", "liga": "Premier League", "pais": "Inglaterra"},
    {"nombre": "Real Madrid", "ciudad": "Madrid", "liga": "La Liga", "pais": "España"},
    {"nombre": "Barcelona", "ciudad": "Barcelona", "liga": "La Liga", "pais": "España"},
    {"nombre": "Bayern Munich", "ciudad": "Munich", "liga": "Bundesliga", "pais": "Alemania"},
    {"nombre": "PSG", "ciudad": "Paris", "liga": "Ligue 1", "pais": "Francia"},
    {"nombre": "Juventus", "ciudad": "Turín", "liga": "Serie A", "pais": "Italia"}
]

# Función para generar nombres aleatorios para las jugadoras
def generar_nombre():
    # Generar un nombre aleatorio de 8 caracteres
    nombre = ''.join(random.choices(string.ascii_lowercase, k=7))
    # Asegurarse de que la primera letra sea mayúscula
    return random.choice(string.ascii_uppercase) + nombre

# Script para crear equipos y jugadores con roles definidos
with driver.session() as session:
    for equipo in equipos:
        # Insertar equipo
        session.run(
            """
            MERGE (e:Equipo {nombre: $nombre, ciudad: $ciudad, liga: $liga, pais: $pais})
            """,
            nombre=equipo["nombre"],
            ciudad=equipo["ciudad"],
            liga=equipo["liga"],
            pais=equipo["pais"]
        )

        # Definir los roles y la cantidad de jugadores para cada equipo
        jugadores_por_rol = {
            "Portera": 1,
            "Defensa Central": 2,
            "Defensa Lateral": 2,
            "Centrocampista Defensivo": 1,
            "Centrocampista Ofensivo": 1,
            "Extremo": 2,
            "Delantera Centro": 1,
            "Delantera Segunda Punta": 1
        }

        # Crear las jugadoras con sus roles y relacionarlas con los equipos
        for rol, cantidad in jugadores_por_rol.items():
            for _ in range(cantidad):
                nombre = generar_nombre()
                edad = random.randint(18, 35)
                start_year = random.randint(2015, 2023)
                nivel_satisfaccion = random.randint(1, 100)

                # Crear nodo Jugadora
                session.run(
                    """
                    CREATE (j:Jugadora {nombre: $nombre, edad: $edad, posicion: $posicion, start_year: $start_year, nivel_satisfaccion: $nivel_satisfaccion})
                    """,
                    nombre=nombre,
                    edad=edad,
                    posicion=rol,
                    start_year=start_year,
                    nivel_satisfaccion=nivel_satisfaccion
                )

                # Relacionar Jugadora con Equipo
                session.run(
                    """
                    MATCH (j:Jugadora {nombre: $nombre}), (e:Equipo {nombre: $equipo_nombre})
                    CREATE (j)-[:JUEGA_EN {start_year: $start_year, nivel_satisfaccion: $nivel_satisfaccion}]->(e)
                    """,
                    nombre=nombre,
                    equipo_nombre=equipo["nombre"],
                    start_year=start_year,
                    nivel_satisfaccion=nivel_satisfaccion
                )

print("Equipos y jugadores creados exitosamente.")
