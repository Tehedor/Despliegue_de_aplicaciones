# Practica Creativa 2


1. Configurar las variables de entorno

```
export SERVICE_VERSION=v1 export GRUPO_NUMERO=09
```
Ver como estan configruadas las varibles de entorno
```
python3 variables_entorno.py
```
2. Inicializar el proyecto para que se descarge y configure todo lo necesario
```
python3 iniciar.py
```


## 1. Despliegue de la aplicación en máquina virtual pesada (2 puntos)
```
cd 1_mv_pesada
```
1. Actualizamos con:
```
python3 script_m_pesada.py configurar
```
2. Arrancar el servidor
```
python3 script_m_pesada.py 
```



## 2. Despliegue de una aplicación monolítica usando docker (2 puntos).

```
cd 2_docker_mono
```
1. Crear la imagen
```
python3 script_docker.py image
```

2. Arrancar el contendor
```
python3 script_docker.py
```

## 3. Segmentación de una aplicación monolítica en microservicios utilizando docker-compose ( 2 puntos)
```
cd 3_docker_seg
```
1. Crearemos las imagenes de details, productpage y ratings 
```
python3 control_docker-compose.py images

```
2. Crearemos la imagen y el contenedor de gradle manualmente para luego poder crear las imagenes de reviews 
```
cd images/reviews/reviews
```
```
sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build
```
```
cd ../../..
```

3. Crearemos todas las versiones de reviews con este comando
```
python3 control_docker-compose.py reviews
```

4. Para ejecutar el docker-compose
```
python3 control_docker-compose.py 
```

+ Cambiar de versiones de reviews
v1
```
export SERVICE_VERSION=v1 
```
v2
```
export SERVICE_VERSION=v2
```
v3
```
export SERVICE_VERSION=v3 
```
Después de cambiar la varible de entorno deberemos de ejecutar de nuevo
```
python3 control_docker-compose.py 
```
+ Otros comandos

Eliminar contenedores
```
python3 control_docker-compose.py eliminar_contenedores
```
Eliminar todo
```
python3 control_docker-compose.py eliminar_todo
```


## 3.5 Opcional. Docker Compose con las imagenes en la nube

```
cd 3.5_docker_nube
```
1. Ejecutaremos directamente el docker-compose, ya que las imagenes sen encuentran en la nube
```
python3 control_coker-compose.py 
```

+ Cambiar de versiones de reviews
v1
```
export SERVICE_VERSION=v1 
```
v2
```
export SERVICE_VERSION=v2
```
v3
```
export SERVICE_VERSION=v3 
```
Después de cambiar la varible de entorno deberemos de ejecutar de nuevo
```
python3 control_docker-compose.py 
```

+ Otros comandos

Eliminar contenedores
```
python3 control_docker-compose.py eliminar_contenedores
```
Eliminar todo
```
python3 control_docker-compose.py eliminar_todo
```


## 4. Despliegue de una aplicación basada en microservicios utilizando Kubernetes (4 puntos)
```
cd 4_kubernetes
```
1. Crear los deployments y services
```
python3 control_kube.py
```
+ Elimnar todo
```
python3 control_kube.py eliminar_todo
```


## 4.5 Opcional, Helm Charts
```
cd 4.5_helm_chart
```
1. Añadir repositorio de charts
```
python3 control_chart.py add_repo
```
2. Arrancar los charts 
```
python3 control_chart.py
```
+ Eliminar todo 
```
python3 control_chart.py eliminar_todo
```

> **Nota:** Charts en el repositorio: https://github.com/Tehedor/helmcharts.git

