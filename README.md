Proyecto NoSQL con Docker

Este proyecto contiene varias bases de datos NoSQL (MongoDB, Cassandra, HBase, InfluxDB, Neo4j) montadas en contenedores Docker y scripts de Python para interactuar con ellas.

Requisitos Previos

Docker y Docker Compose: Para levantar los contenedores.

Python 3 y Pip: Para ejecutar los scripts de Python.

Git: Para clonar el repositorio.

Instrucciones para Ejecutar el Proyecto

1. Clonar el Repositorio

git clone https://github.com/UnaiLaconcha/databasesNoSQL.git
cd databasesNoSQL

2. Levantar los Contenedores

Cada base de datos tiene su propia configuración de Docker Compose. Navega a cada carpeta y ejecuta:

MongoDB:

cd MongoDB
docker-compose up -d

Cassandra:

cd ../Cassandra
docker-compose up -d

InfluxDB:

cd ../InfluxDB
docker-compose up -d

HBase:

cd ../HBase
docker-compose up -d

Neo4j:

cd ../Neo4j
docker-compose up -d

3. Crear y Activar un Entorno Virtual

En la carpeta principal del proyecto:

python3 -m venv venv
source venv/bin/activate  # Linux/WSL2/Mac

4. Instalar las Dependencias de Python

Con el entorno virtual activado:

pip install pymongo cassandra-driver influxdb neo4j

5. Ejecutar los Scripts de Inserción y Consulta

Navega a la carpeta scripts para ejecutar los scripts correspondientes:

cd scripts

# Insertar y consultar datos en MongoDB
python MongoDBinsercion.py
python MongoDBconsultas.py

# Insertar y consultar datos en Cassandra
python Cassandrainsercion.py
python Cassandraconsultas.py

Detalles Adicionales

Cada contenedor está configurado para exponer los puertos estándar de cada base de datos. Asegúrate de que los puertos (como el 27017 para MongoDB) no estén ocupados por otros servicios en tu máquina.

Recuerda que cada base de datos tiene su archivo docker-compose.yml independiente, lo cual te permite levantar y detener cada base de datos según sea necesario.

Utilizar un entorno virtual para Python es opcional, pero altamente recomendado para evitar conflictos con otras librerías de Python instaladas globalmente.

Contacto

Si tienes alguna pregunta o encuentras algún problema, no dudes en abrir un issue en el repositorio o contactar al autor.

