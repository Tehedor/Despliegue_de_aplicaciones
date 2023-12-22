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


## 3. Segmentación de una aplicación monolítica en microservicios utilizando docker-compose ( 2 puntos)
```
cd 3_docker_sef
```
```
cd images/reviews/reviews
```
```
docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build
```

```
cd ../../...
```

Para crear las imagenes que va a utilizar el docker-compose
```
python3 control_coker-compose.py images
```

Para ejecutar el docker-compose
```
python3 control_coker-compose.py 
```



## 3.5 Opcional. Docker Compose con las imagenes en la nube

```
cd 3.5_docker_nube
```

## 4. Despliegue de una aplicación basada en microservicios utilizando Kubernetes (4 puntos)
```
cd 4_kubernetes
```

## 4.5 Opcional, Helm Charts
