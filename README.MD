# Proyecto de preddicon con mineria de datos
## Instalacion
En caso sea la primera vez que se descargue el proyecto; ejecute cada linea una por una:
```
git clone https://github.com/JosueCumpa/pryAbrahamV1.git 
cd pryAbrahamV1 
git branch N_su_rama
git checkout N_su_rama
py -3 -m -venv 
.venv\script\activate
pip install Flask psycopg2
```
## Guardar cambios
Guardar cambios del proyecto
```	
git checkout N_su_rama
git add .
git commit -m "Update"
git push -u origin N_su_rama
```

## Caso de descargar el proyecto actualizado
```
git pull origin main o master o N_su_rama
```
## Publicar con NGROK para pruebas
* instalar Ngrok (Recomendado para publicar proyecto de pruebas)
* abrir un cmd en la carpeta raiz del NGROK
* ingregar la clave que te da la pagina una vez que te registrar en el cmd
* Una vez configurado ejecuitar:
```ngrok http "Puerto-Escucha"```	


## Colaboradores - ing de sistemas y computacion - 8 ciclo
#### CUMPA CHANCAFE JOSUE GIANCARLOS 


