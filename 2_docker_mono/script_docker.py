from os import environ,path,sys,chdir
from subprocess import call,run,check_output
import os

segundo_argumento = ""
if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]

################  Help  ################
if segundo_argumento == "-h" or segundo_argumento == "--help":
    print("""
        ((( Ojo ))) 
            Variable de entorno: GRUPO_NUMERO
            -> export GRUPO_NUMERO=09

    Uso:    script_docker.py [opcion] 
    opcion:
        " " (vacío)             -> Arrancar en el puerto 9080
        eliminar_contenedores   -> Eliminar los contenedores
        eliminar_todo           -> Eliminar los contenedores y images
        image                   -> Crear imagen de productpage
    """)
    exit(0)

    
# ######################################################################################################################
# Eliminar contenedores y imagenes
# ######################################################################################################################
if segundo_argumento == "eliminar_todo":

    container_ids = check_output(["sudo", "docker", "ps", "-a", "-q"])
    if container_ids:
        for id in container_ids.split():
            call(["sudo", "docker", "stop", id])
            call(["sudo", "docker", "rm", id])

    images_ids = check_output(["sudo", "docker", "images", "-q"])
    if images_ids:
        for id in images_ids.split():
            call(["sudo", "docker", "rmi", id])

    exit(0)

# ######################################################################################################################
# Eliminar contendedores
# ######################################################################################################################
elif segundo_argumento == "eliminar_contenedores":

    container_ids = check_output(["sudo", "docker", "ps", "-a", "-q"])
    if container_ids:
        for id in container_ids.split():
            call(["sudo", "docker", "stop", id])
            call(["sudo", "docker", "rm", id])

    exit(0)

# ######################################################################################################################
# Crear Imagen
# ######################################################################################################################
elif segundo_argumento == "image":
    chdir('productPage_mono')
    call(["python3","control_docker.py"])      
    exit(0)

# ######################################################################################################################
# Arrancar en el puerto 9080
# ######################################################################################################################
varibaleGroup =  environ.get('GRUPO_NUMERO')

call(["sudo","docker","run","-d","--name","productpage-mono","-p","9080:9080", varibaleGroup + "/productpage:mono" ]) 
