# GESTION DE TIENDA
Aplicacion para gestionar la base de datos de una tienda
## Procedimiento de arranque
Sigue los pasos para poder inciar la aplicacion en tu equipo
## Ajustes iniciales
Abra un terminal en el directorio del proyecto y ejecute el siguiente comando para crear un entorno virtual:
```
python -m virtualenv .venv
```
.venv es el nombre de la carpeta del entorno virtual(modifiquelo al gusto)

Active el entorno virtual con el siguiente comando(Ubuntu):
```
source .venv/bin/activate
```
(Windows):
```
.venv\Scripts\activate
```
Cambie el .venv si no le ha llamado asi a la carpeta

Instale las dependencias con el siguiente comando:
```
pip install -r requirements.txt
```
Cree un arhivo con el nombre **.env**  en **/Tienda** especifique los datos de configuracion de la base de datos que va a usar, habiendo creado una base de datos llamada Tienda:
```
SECRET_KEY=djangoSecretKey
DB_NAME=dbname
DB_USER=dbuser
DB_PASSWROD=dbpassword
DB_HOST=dbhost
DB_PORT=dbport
```
Una vez realizada la configuracion de la base de datos haga las migraciones:
```
python manage.py migrate
```
## Puesta en marcha
Ejecute el comando:
```
python manage.py runserver
```
Seleccione la opcion de Django si se le pregunta

Ahora acceda a la direccion que se le indica(en mi caso seria):

http://127.0.0.1:8000/

## Esturctura del proyecto

Modulo principal **manage.py**

Los html se encuentran en **/administrador/templates**

Los estilos se encuentran en **/administrador/static/css**

el archivo requirements se encuentran en **requirements.txt**