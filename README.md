# Cloud project: Movie Recommendator
## Descripción
Nuestro proyecto consiste en un programa capaz de recomendar películas de acuerdo a diferentes variables que pida el usuario. Por ejemplo, dependiendo del género, el año, etc. También puede recomendar si una película dada por el usuario es recomendable o no en base a las valoraciones de los usuarios.
Para ello, el usuario debe especificar siempre sobre qué tipo de dataset quiere consultar. El recomendador puede realizar recomendaciones en base a los datasets de las páginas web de MovieLens (https://grouplens.org/datasets/movielens/) e IMDb (https://www.imdb.com/interfaces/). 

## Descarga de archivos
Todos nuestros scripts de tratamiento de datos se encuentran en la carpeta _scripts_. Con respecto a los datasets, debido alelevado tamaño de los datasets empleados (más de 1 GB en total entre todos), hemos tenido que crear un script de Python que, al ejecutarlo, descargará todos los datasets de sus páginas originales a la carpeta _script_ en el directorio local del usuario. Por ello, es necesario que el usuario, antes de ejecutar algún

Antes que nada, es necesario descargar ambas carpetas y descomprimirlas en local. Una vez descomprimidas, es necesario mover todo el contenido de la carpeta _datasets_ (es decir, todos los datasets) a la carpeta _scripts_. Después de realizar la descarga y mover todos los archivos a la carpeta _scripts_, comienza la preparacion del entorno.

## Preparación del entorno
Para poder ejecutar los scripts de Python, es necesario tener instalado Python y un intérprete de comandos de tipo Unix. Este intérprete puede ser Linux, una máquina de Google Cloud o WSL en caso de que se quiera ejecutar estos scripts en local y el Sistema Operativo sea Windows.
En cuanto a Python, por lo general, viene ya pre-instalado en el sistema. Para poder tener la versión más actualizada, es necesario ejecutar el siguiente comando:
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
<BORRAR LUEGO: Seguir la continuación: https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server>
Para poder ejecutar los scripts correctamente, es necesario importar los siguientes módulos de Python:
	*
	*
	*


Para importar estos módulos y revisar si han sido correctamente importados, debe seguir esta serie de pasos:
Debe activar el ambiente de Python:
```
$ source <environment_name>/bin/activate
```
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
Si desea salir del ambiente de Python, debe ejecutar el siguiente comando:
```
$ deactivate
```
## Instalación de Pyspark

## Ejecución

## Links
* Github Pages
  * Documentación: https://pages.github.com/
  * Documentación: https://docs.github.com/en/pages 
  * Link de la página web: https://softwarestacklukas.github.io/group7.github.io/ 
