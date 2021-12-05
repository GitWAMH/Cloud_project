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
sudo apt -y upgrade
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
$sudo apt install -y python3-venv
```
Después, el usuario debe escoger qué carpeta quiere usar para esteblecer el ambiente de programación de Python. Puede ser cualquier carpeta. En nuestro ejemplo, usaremos una carpeta que se llama _environments_. Hay que entrar a la carpeta (```$ cd environments```) y ya dentro de la carpeta, se ejecuta el siguiente comando para establecer el ambiente de Python:
```
$ python3 -m venv my_env
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
* Módulo requests
* Módulo datetime
* Módulo gzip
* Módulo shutil
* Módulo zipfile
* Módulo pyspark
* Módulo sys
* Módulo re
        
Para importar estos módulos y revisar si han sido correctamente importados, debe seguir esta serie de pasos:
Debe activar el ambiente de Python con los comandos mencionados anteriormente.

Para poder revisar si un módulo está instalado o no, hay que abrir primero la shell the Python:
```
$ python
```
Una vez se ha cargado al shell de Python, escribimos el siguiente comando para revisar si el módulo está instalado o no:
```
>> import <module_name>
```
Si no se muestra ningún mensaje, eso significa que el módulo esta instalado correctamente.
Si sale un mensaje de error, entonces el módulo no está importado. 
Para importar un módulo es necesario salir de la Shell de Python, y ejecutar en la terminal del WSL.
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
## Descarga de archivos

Todos nuestros scripts de tratamiento de datos se encuentran en la carpeta _scripts_. Con respecto a los datasets, debido alelevado tamaño de los datasets empleados (más de 1 GB en total entre todos), se ha creado un script de Python llamado _download_datasets.py_ que, al ejecutarlo, descargará todos los datasets de sus páginas originales a la carpeta _script_ en el directorio local del usuario. Por ello, es necesario que el usuario, antes de ejecutar algún script, deba ejecutar el script _downloads_datasets.py_ para poder descargar los datasets en local. Después de ejecutar este script, se puede comenzar la ejecuación de la aplicación.

## Ejecución


## Links
* Github Pages
  * Documentación: https://pages.github.com/
  * Documentación: https://docs.github.com/en/pages 
  * Link de la página web: https://softwarestacklukas.github.io/group7.github.io/ 
