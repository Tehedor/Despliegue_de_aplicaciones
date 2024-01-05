from os import environ,path,sys
from subprocess import call,run
import os
import getpass


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
    volumes = check_output(["sudo", "docker", "volume", "ls", "-q"])
    if volumes:
        for id in volumes.split():
            call(["sudo", "docker", "volume","rm", id])
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
print("#### SERVICE_VERSION=" + environ.get('SERVICE_VERSION') + " ####\n")
print("export SERVICE_VERSION=v1\n")
print("export SERVICE_VERSION=v2\n")
print("export SERVICE_VERSION=v3\n")
