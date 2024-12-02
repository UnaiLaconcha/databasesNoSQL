<h1>Práctica: Análisis de Dinámica de Equipos Deportivos con Neo4j</h1>

<h2>Introducción</h2>
<p>
    Este proyecto tiene como objetivo modelar y analizar las relaciones dentro de equipos de fútbol femeninos que participan en la Liga Conferencia de la UEFA. Utilizando Neo4j, se busca comprender las dinámicas de trabajo en equipo y cómo estas afectan al rendimiento deportivo de las jugadoras, con un enfoque en la representación visual y el análisis eficiente de relaciones complejas. Este estudio servirá como punto de partida para un análisis más profundo en futuras fases.
</p>

<h2>Configuración e Instrucciones de Ejecución de Neo4j</h2>
<p>
    Para ejecutar la interfaz visual de Neo4j y trabajar con los datos de la práctica, se deben seguir los siguientes pasos:
</p>
<ol>
    <li><strong>Abrir WSL2:</strong> Asegúrate de tener WSL2 instalado y configurado en tu sistema.</li>
    <li><strong>Crear una Carpeta para el Proyecto:</strong> En la terminal de WSL2, crea una carpeta llamada <code>databasesNoSQL</code> y accede a ella:
        <pre>mkdir databasesNoSQL<br>cd databasesNoSQL</pre>
    </li>
    <li><strong>Clonar el Repositorio:</strong> Clona el repositorio de GitHub donde se encuentran los scripts necesarios para el proyecto y accede a él:
        <pre>git clone https://github.com/UnaiLaconcha/databasesNoSQL.git <br>cd databasesNoSQL</pre>
    </li>
    <li><strong>Crear y Activar un Entorno Virtual:</strong> En la carpeta principal del proyecto, crea y activa un entorno virtual de Python para gestionar las dependencias de forma aislada:
        <pre>python3 -m venv venv<br>source venv/bin/activate</pre>
    </li>
    <li><strong>Instalar las Dependencias de Python:</strong> Con el entorno virtual activado, instala las dependencias necesarias para el proyecto, incluyendo el controlador de Neo4j y otros módulos:
        <pre>pip install neo4j datetime</pre>
    </li>
    <li><strong>Acceder a la Carpeta de Neo4j:</strong> Dentro del repositorio clonado, accede a la carpeta <code>neo4j</code> donde está el archivo <code>docker-compose.yml</code> con la configuración del contenedor Neo4j.</li>
    <li><strong>Lanzar el Contenedor:</strong> Ejecuta el siguiente comando para lanzar el contenedor con Docker:
        <pre>docker-compose up</pre>
    </li>
    <li><strong>Abrir Otra Terminal:</strong> Mientras el contenedor está corriendo, abre otra terminal de Ubuntu y ejecuta el siguiente comando para verificar que el contenedor se está ejecutando correctamente:
        <pre>docker ps</pre>
        Esto mostrará información sobre el contenedor en ejecución, incluyendo el nombre <code>neo4j_db</code> y los puertos asignados.
    </li>
    <li><strong>Obtener la Dirección IP del Contenedor:</strong> Abre una terminal de WSL2 y ejecuta el siguiente comando para obtener la dirección IP del contenedor:
        <pre>ip addr | grep eth0</pre>
        Esto debería mostrar algo similar a: <code>inet 172.25.176.1/20 brd 172.25.191.255 scope global eth0</code>
    </li>
    <li><strong>Abrir la Interfaz Visual de Neo4j:</strong> Utiliza la dirección IP obtenida y el puerto <code>7474</code> para acceder a la interfaz visual de Neo4j en tu navegador:
        <pre>http://172.25.176.1:7474</pre>
    </li>
    <li><strong>Acceder a la Cuenta de Neo4j:</strong> Una vez en la interfaz visual, utiliza las credenciales definidas en el archivo <code>docker-compose.yml</code> para acceder:
        <ul>
            <li>Usuario: <code>neo4j</code></li>
            <li>Contraseña: <code>entrega2</code></li>
        </ul>
    </li>
</ol>

<h2>Conclusiones</h2>
<p>
    Este proyecto ha establecido una base sólida para la representación de datos complejos utilizando Neo4j. Se ha demostrado la capacidad de Neo4j para modelar relaciones complejas de forma intuitiva y eficiente, lo cual es fundamental en el análisis de dinámicas sociales como las del trabajo en equipo en el contexto deportivo. Aunque esta práctica se ha centrado principalmente en la configuración y almacenamiento de datos, el modelo establecido proporciona un punto de partida excelente para futuros análisis detallados del comportamiento cooperativo en equipos de fútbol.
</p>
