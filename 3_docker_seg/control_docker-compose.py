from os import environ,path,sys
from subprocess import call,run,check_output
import os
import getpass


# ######################################################################################################################
# Añadir files necesario para el funcionamiento de las aplicaciones
# ######################################################################################################################
if not path.exists("./images/details/details"):
    call(["cp","-r","../practica_creativa2/bookinfo/src/details","./images/details/"])

if not path.exists("./images/productPage_seg/productpage"):
    call(["cp","-r","../practica_creativa2/bookinfo/src/productpage","./images/productPage_seg/"])
    
if not path.exists("./images/ratings/ratings"):
    call(["cp","-r","../practica_creativa2/bookinfo/src/ratings","./images/ratings/"])

if not path.exists("./images/details/reviews"):
    call(["cp","-r","../practica_creativa2/bookinfo/src/reviews","./images/reviews/"])


segundo_argumento = ""
if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]

################  Help  ################
if segundo_argumento == "-h" or segundo_argumento == "--help":
    print("""
        ((( Ojo ))) 
            Variable de entorno: GRUPO_NUMERO
            e.g -> export GRUPO_NUMERO=09
            Variable de entorno: SERVICE_VERSION
            e.g -> export SERVICE_VERSION=v1

    Uso:    control_docker-compose.py [opcion] 
    opcion:
        " " (vacío)             -> Iniciar y ejecutar los contenedores
        eliminar_contendores    -> Eliminar los contenedores
        eliminar_todo           -> Eliminar los contenedores y los volumes
        images                  -> Crear imagenes de details, productpage y ratings
        reviews                 -> Crear imagenen de reviews

    ¡¡¡¡¡  Importante  !!!!!    
        Antes de opción "review":
            1. Ir al directorio: images/reviews/reviews
            2. Ejecutar: sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build
    
    
    Cambiar version de los servicios:
        export SERVICE_VERSION=v1
        export SERVICE_VERSION=v2
        export SERVICE_VERSION=v3
    
    """)
    exit(0)


# ######################################################################################################################
# Elimanar contenedores 
# ######################################################################################################################
if segundo_argumento == "eliminar_contendores":
    call(["sudo","docker-compose","down"])
    exit(0)


# ######################################################################################################################
# Elimnar contenedores y volumes
# ######################################################################################################################
if segundo_argumento == "eliminar_todo":
    call(["sudo","docker-compose","down"])
    if volumes:
        for id in images_names.split():
            call(["sudo", "docker", "volume","rm", id])
    exit(0)

# ######################################################################################################################
# Crear imagenes de details, productpage y ratings
# ######################################################################################################################
if segundo_argumento == "images":
    call(["python3","images/details/control_docker.py","create"])
    call(["python3","images/productPage_seg/control_docker.py","create"])
    call(["python3","images/ratings/control_docker.py","create"])
    exit(0)

# ######################################################################################################################
# Crear imagenen de reviews
# ######################################################################################################################
if segundo_argumento == "reviews":
    call(["python3","images/reviews/control_docker.py","create"])
    exit(0)

# ######################################################################################################################
# Crear variables de entorno para docker-compose
# ######################################################################################################################
call(["python3","env.py"])

# ######################################################################################################################
# Inicia y ejecuta los contenedores
# ######################################################################################################################
call(["sudo","docker-compose","up","-d"])


# Mostar versions de los servicios y las posibles convinaciones que hay
print("#### SERVICE_VERSION=" + environ.get('SERVICE_VERSION' + " ####\n"))
print("export SERVICE_VERSION=v1\n")
print("export SERVICE_VERSION=v2\n")
print("export SERVICE_VERSION=v3\n")