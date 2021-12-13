# Cloud project: Movie Recommendator
## Descripción
Nuestro proyecto consiste en un programa capaz de recomendar películas de acuerdo a diferentes variables que pida el usuario. Por ejemplo, dependiendo del género, el año, etc. También puede recomendar si una película dada por el usuario es recomendable o no en base a las valoraciones de los usuarios.
Para ello, el usuario debe especificar siempre sobre qué tipo de dataset quiere consultar. El recomendador puede realizar recomendaciones en base a los datasets de las páginas web de MovieLens (https://grouplens.org/datasets/movielens/) e IMDb (https://www.imdb.com/interfaces/). 

## Instalación de Python y preparación del entorno
Para poder ejecutar los scripts de Python, es necesario tener instalado Python y un intérprete de comandos de tipo Unix. Este intérprete puede ser Linux, una máquina de Google Cloud o en usando el WSL de Windows.
Python, por lo general, ya viene pre-instalado en el sistema. Para poder tener la versión más actualizada, es necesario ejecutar el siguiente comando
```
$ sudo apt update
```
Después necesitamos actualizarlos en el sistema para así poder tener la versión más moderna:
```
$ sudo apt -y upgrade
```
La opción -y se usa para que automáticamente se acepte todos los archivos que se están descargando. Aún así, cabe la posibilidad de que existan algunos paquetes que requieran de una aprobación explícita del usuario.

Después de actualizar los paquetes, puede revisar la versión de Python mediante el comando:
```
$ python3 -V
Python 3.8.10
```
Si aún así sale error, intente instalar Python3 directamente mediante la ejecución de los siguientes comandos:
```
$sudo apt-get update
$sudo apt-get install python3.8
```
En segundo lugar, habría que instalar el comando pip, para poder gestionar los paquetes de Python:
```
$ sudo apt install -y python3-pip
```
Esto permite utilizar tanto el comando pip, como pip3 para instalar y gestionar módulos.
Una vez instalado la el comando pip, es necesario establecer un ambiente virtual de Python, para ello, se tiene que instalar el módulo _venv_ mediante este comando:
```
$ sudo apt install -y python3-venv
```
Para poder usar el comando python en lugar de python3 es necesario instalar un paquete llamado python-is-python3, ejecutando:
```
$ sudo apt install python-is-python3
```
Después, el usuario debe escoger qué carpeta quiere usar para esteblecer el ambiente de programación de Python. Puede ser cualquier carpeta. En nuestro ejemplo, usaremos una carpeta que se llama _environments_. Hay que entrar a la carpeta (```$ cd environments```) y ya dentro de la carpeta, se ejecuta el siguiente comando para establecer el ambiente de Python:
```
$ python -m venv my_env
```
Tras esto, cada vez que el usuario quiera activar el ambiente de Python, debe activar el siguiente comando:
```
$ source <environment_name>/bin/activate
```
Y cada vez que el usuario quiera salir del ambiente, deberá ejecutar el siguiente comando
```
$ deactivate
```
## Módulos necesarios e importación
Para poder ejecutar los scripts correctamente, es necesario importar los siguientes módulos de Python:

* Módulo os
* Módulo requests
* Módulo datetime
* Módulo gzip
* Módulo shutil
* Módulo zipfile
* Módulo pyspark
* Módulo sys
* Módulo re
* Módulo pyfiglet
        
Para importar estos módulos y revisar si han sido correctamente importados, debe seguir esta serie de pasos:
Debe activar el ambiente de Python con los comandos mencionados anteriormente.

Para poder revisar si un módulo está instalado o no, hay que abrir primero la shell the Python:
```
$ python
```
Si no funciona este comando, intenta con el siguiente comand:
```
$ python3
```
Una vez se ha cargado al shell de Python, escribimos el siguiente comando para revisar si el módulo está instalado o no:
```
>> import <module_name>
```
Si no se muestra ningún mensaje, eso significa que el módulo esta instalado correctamente.
Si sale un mensaje de error, entonces el módulo no está importado. 
Para importar un módulo es necesario salir de la Shell de Python e instalar el módulo con el comando pip:
```
$ pip install <module_name>
```
Una vez instalado, volver a entrar a la shell de Python y revisar de nuevo si está instalado el módulo o no.
```
$ python
>> import <module_name>
```
## Instalación de Pyspark
En primer lugar, se debe instalar Java:
```
$ sudo apt update
$ sudo apt install default-jre
```
Después, instalar la distribución a de Apache Spark en una carpeta llamada /usr/local/spark
```
$ curl -O https://ftp.cixug.es/apache/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
$ tar xvf spark-3.1.2-bin-hadoop3.2.tgz
$ sudo mv spark-3.1.2-bin-hadoop3.2 /usr/local/spark
```
Después modificar el archivo ~/.profile con el comando ```$ nano ~/.profile``` para añadir la variable
```
PATH = "$PATH:/usr/local/spark/bin"
```
Y actualizar la variable PATH en la sesión actual.
```
source ~/.profile
```
Tras esto, podrá ejecutar cualquiera de los scripts de la aplicación a través de Apache Spark mediante el siguiente comando:
```
$ spark-submit <nombre_archivo.py> [argumentos]
```

## Detalles de cada script

En esta sección se describe para qué sirve cada script y los argumentos que deben proporcionarse:
* adult_child_movies.py. Devuelve, dependiendo del parámetro introducido, películas clasificadas para adultos o aptas para niños ordenadas por valoración. Los argumentos que usa son:
    * Opción: -a para buscar películas para adultos o -c para buscar películas para niños.
    * El número de películas que quieres que se muestren (Opcional).
* best_rated_movies_by_year.py. Devuelve las películas mejor valoradas de un año que se pasa por parámetro. Sus argumentos son:
    * Modo: -m para buscar en los datasets de MovieLens o -i para buscar en los datasets de IMDb.
    * El año al que pertenecen las películas que se buscan.
    * El número de películas que quieres que se muestren (Opcional).
* best_runtime.py. Devuelve las películas que tienen una duración dentro de los parámetros proporcionados por el usuario, ordenadas por valoración. Todos los argumentos de este script son opcionales, ya que cuenta con valores por defecto:
    * La valoración mínima que el usuario espera.
    * El tiempo de duración mínimo.
    * El tiempo de duración máximo.
    * El número de recomendaciones que se mostrarán por pantalla.
    * Un argumento que especifica información extra que se quiere mostrar, que puede ser:
        * -avg: la duración media.
        * -max: la duración máxima.
        * -min: la duración mínima.
        * -sum: el sumatorio de duraciones.
* download_datasets. Este script se utiliza para desacrgar los datasets que se van a procesar. No requiere de ningún argumento.
* getRatingsPerImdbType.py. Devuelve las mejores películas que pertenecen a un tipo de IMDb, especificado por el usuario. Sus argumentos son:
    * -h o -help para visualizar los tipos de IMDb entre los que elegir.
    * El tipo de IMDb con el que se quiere filtrar.
    * El nivel de valoración.
    * El número de recomendaciones que se mostrarán por pantalla.
* main.py. Este script permite al usuario ejecutar cualquiera de los scripts de procesamiento de datos mediante un menú, así como seleccionar dónde quiere ejecutar esos scripts, de una manera más sencilla y sin usar comandos. No requiere de ningún argumento.
* movies_by_genre.py. Devuelve las películas pertenecientes a un género, proporcionado por el usuario, ordenadas por valoración. Sus argumentos son:
    * Modo: -m para buscar en los datasets de MovieLens o -i para buscar en los datasets de IMDb.
    * El género cinematográfico por el que se filtrarán las películas.
    * El número de películas que quieres que se muestren (Opcional).
* movies_by_title.py. Devuelve las películas que tienen un título que contiene las palabras proporcionadas por el usuario, ordenadas por valoración. Sus argumentos son:
    * El título de la película que quieres buscar.
* worth_movie.py. En base a las valoraciones de los usuarios, decide si una película merece o no la pena ver. Sus argumentos son:
    * El título de la película por el que quieres consultar si vale la pena. 
* year_region_recommendations.py. Deveuelve las mejores películas de un año o una región proporcionada por el usuario. Sus argumentos son:
    * El año o la región sobre la que se quiere consultar.
    * El número de películas que quieres que se muestren (Opcional).

## Descarga de archivos

Todos nuestros scripts de tratamiento de datos se encuentran en la carpeta _scripts_. Con respecto a los datasets, debido al elevado tamaño de los datasets empleados (más de 1 GB en total entre todos), se ha creado un script de Python llamado _download_datasets.py_ que, al ejecutarlo, descargará todos los datasets de sus páginas originales a la carpeta _scripts_ en el directorio local del usuario. Por ello, es necesario que el usuario, antes de ejecutar algún script, ejecute el script _download_datasets.py_ para poder descargar los datasets en local. Después de ejecutar este script, se puede comenzar la ejecución de la aplicación.

## Ejecución

Para ejecutar nuestros scripts (incluyendo el _download_datasets.py_) de manera individual puede utilizarse el comando:
```
$ spark-submit <nombre_archivo.py> [argumentos]
```
Sin embargo una opción más simple es utilizar el script _main.py_ que contiene un menú con el que interactuar de forma más sencilla con los scripts. Esto se haría ejecutando:
```
$ python main.py
```
Sino también se puede ejecutar con el siguiente comando:
```
$ python3 main.py
```
**Importante**:¨Este comando se debe ejecutar sin haber activado el ambiente de Python.

Desde _main.py_ los scripts se ejecutan en Spark en modo local y antes de mostrar las opciones se pide al usuario que introduzca el número de cores de su procesador que desea utilizar para la ejecución. Si el usuario desea ejecutar la aplicación en Google Cloud, más adelante se explica cómo hacerlo.

Después de elegir el número de cores, se mostrará por pantalla un menú como éste:
```
0 -- Download Datasets (Essential)
1 -- Movies for adults or children
2 -- Best rated movies by year
3 -- Best runtime
4 -- Ratings per IMDb type
5 -- Best movies from a given genre
6 -- Best movies from a given title
7 -- Is it worth to watch this movie?
8 -- Best movies by year and region
9 -- Exit
Enter your choice: 
```
El usuario únicamente tiene que escribir el número de la opción que quiera ejecutar e introducir los argumentos requeridos, pudiendo dejar en blanco los opcionales. Antes de ejecutar cualquier script, es imprescindible descargar los datasets ejecutando el script _download_datasets.py_ o bien desde el propio menú con la opción cero.

Los scripts se ejecutan en Spark y se puede utilizar la opción SparkSession.builder.master para elegir el modo de ejecución, cuyo parámetro es la URL del Spark master:
* Local: Ejecuta localmente.
* Local[N]: Ejecuta localmente utilizando N cores.
* Local[*]: Ejecuta localmente utilizando todos los cores disponibles de la máquina.
* La URL del cluster de spark sobre el que se quiere ejecutar el script (Ej.:“spark://master:7077”).

En caso de querer ejecutar los scripts en _Google Cloud_ deben seguirse los siguientes pasos:
1. Crear el Dataproc Cluster ejecutando este comando en el Cloud Shell:
```
$ gcloud dataproc clusters create example-cluster --enable-component-gateway --region europe-west6 --zone europe-west6-b --master-machine-type n1-standard-4 --master-boot-disk-size 50 --num-workers 2 --worker-machine-type n1-standard-4 --worker-boot-disk-size 50 --image-version 2.0-debian10
```
2. Crear un nuevo bucket en la sección Cloud Storage.
3. Cargar todos los scripts en el Dataproc Cluster
4. Cargar todos los ficheros en el bucket creado.
5. Modificar todos los scripts de Python, cambiando el directorio de los datasets a _gs://<BUCKET_NAME>/<MOVIE_LENS_FOLDER_NAME>/<MOVIELENS_DATASET_NAME>_ o _gs://<BUCKET_NAME>/<IMDB_DATASET_NAME>_.

## Links
Link de la página web en Github Pages: https://rafalonsog.github.io/group7.github.io/

Link del repositorio de la página web: https://github.com/rafalonsog/group7.github.io/tree/Draft
