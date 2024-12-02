from neo4j import GraphDatabase
import random
from datetime import datetime, timedelta

# Configuración para conectarse a la base de datos Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"
password = "entrega2"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Script 2: Definición de partidos y relaciones entre equipos y jugadoras
def definir_partidos():
    equipos = ['Manchester City', 'Real Madrid', 'Barcelona', 'Bayern Munich', 'PSG', 'Juventus']
    # Generar partidos entre equipos
    for i in range(12):  # Definimos 10 partidos
        # Seleccionar equipos aleatorios para el partido
        equipo1 = random.choice(equipos)
        equipo2 = random.choice([e for e in equipos if e != equipo1])  # Asegura que los equipos no sean los mismos

        # Definir fecha aleatoria dentro de un rango (puedes cambiar las fechas según sea necesario)
        start_date = datetime(2024, 1, 1)
        random_days = random.randint(0, 365)
        partido_fecha = start_date + timedelta(days=random_days)

        # Resultado aleatorio del partido
        goles_equipo1 = random.randint(0, 5)
        goles_equipo2 = random.randint(0, 5)
        resultado = f'{equipo1} {goles_equipo1} - {goles_equipo2} {equipo2}'

        # Crear el nodo Partido
        with driver.session() as session:
            session.run(
                """
                CREATE (p:Partido {id_partido: $id_partido, fecha: $fecha, resultado: $resultado})
                """,
                id_partido=i + 1,  # ID único para cada partido
                fecha=partido_fecha.strftime('%Y-%m-%d'),
                resultado=resultado
            )

            # Crear relación de competencia entre equipos (Equipos vs Partidos)
            session.run(
                """
                MATCH (e1:Equipo {nombre: $equipo1}), (e2:Equipo {nombre: $equipo2}), (p:Partido {id_partido: $id_partido})
                CREATE (e1)-[:COMPITIO_EN {resultado: $resultado}]->(p)
                CREATE (e2)-[:COMPITIO_EN {resultado: $resultado}]->(p)
                """,
                equipo1=equipo1,
                equipo2=equipo2,
                id_partido=i + 1,
                resultado=f'{goles_equipo1}-{goles_equipo2}'
            )

            # Relacionar jugadoras con partidos
            # Obtener una lista de jugadoras para cada equipo participante
            for equipo in [equipo1, equipo2]:
                jugadores_query = session.run(
                    """
                    MATCH (j:Jugadora)-[:JUEGA_EN]->(e:Equipo {nombre: $equipo})
                    RETURN j.nombre AS nombre, j.posicion AS posicion
                    """,
                    equipo=equipo
                )

                for registro in jugadores_query:
                    jugadora_nombre = registro["nombre"]
                    posicion = registro["posicion"]
                    goles = random.randint(0, 3) if posicion in ["Delantera Centro", "Delantera Segunda Punta", "Extremo"] else 0

                    # Crear la relación entre jugadora y partido
                    session.run(
                        """
                        MATCH (j:Jugadora {nombre: $jugadora}), (p:Partido {id_partido: $id_partido})
                        CREATE (j)-[:PARTICIPA_EN {posicion: $posicion, goles: $goles}]->(p)
                        """,
                        jugadora=jugadora_nombre,
                        id_partido=i + 1,
                        posicion=posicion,
                        goles=goles
                    )

# Llamar a la función para definir los partidos y las relaciones
definir_partidos()