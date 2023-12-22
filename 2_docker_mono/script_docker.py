from os import environ,path,sys,chdir
from subprocess import call,run,check_output
import os


if not path.exists("./practica_creativa2"):
    # Instalar y actualizar todo lo necesario para que funcione la practica
    call(["sudo","apt-get","update"])
    call(["sudo","apt-get","install","python3","-y"])
    call(["sudo","apt-get","install","python3-pip","-y"])
    call(["sudo","apt-get","install","docker.io","-y"])
    call(["sudo","apt-get","install","docker-compose","-y"])


    # Configurar todo el directorio para que funcione de manera adecuda toda la practica
    call(["git","clone","https://github.com/CDPS-ETSIT/practica_creativa2.git"])
    call(["python3","config_requirements.py"])
    call(["python3","config_page.py"])


segundo_argumento = ""
if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]

if segundo_argumento == "resetearfull":

    # Get the IDs of all containers
    container_ids = check_output(["sudo", "docker", "ps", "-a", "-q"])

    # Remove all containers
    if container_ids:
        for id in container_ids.split():
            call(["sudo", "docker", "stop", id])
            call(["sudo", "docker", "rm", id])

    images_ids = check_output(["sudo", "docker", "images", "-q"])

    # Remove all containers
    if images_ids:
        for id in images_ids.split():
            call(["sudo", "docker", "rmi", id])

    exit(0)
elif segundo_argumento == "resetear":
    
    # Get the IDs of all containers
    container_ids = check_output(["sudo", "docker", "ps", "-a", "-q"])

    # Remove all containers
    if container_ids:
        for id in container_ids.split():
            call(["sudo", "docker", "stop", id])
            call(["sudo", "docker", "rm", id])

    images_ids = check_output(["sudo", "docker", "images", "-q"])


    # call(["sudo docker rm $(sudo docker ps -a -q)"])
    #  ponme este comando con call para que funcione: sudo docker rm $(sudo docker ps -a -q)
    # call(["sudo docker rm $(sudo docker ps -a -q)"])
    # call(["sudo docker rmi $(sudo docker images -q)"])
    # sudo docker rmi $(sudo docker images -q)
    exit(0)

varibaleGroup =  environ.get('GRUPO_NUMERO')

# Configurar copiar los files necesario para hacer la imagen de docker file



# Hacer que el script de docker/control_docker.py se ejecute dentro del directorio docker, no desde donde me encuentro ahora
chdir('docker-compose/productPage_mono')
call(["python3","control_docker.py"])  

call(["sudo","docker","run","-d","--name","productpage:mono","-p","9080:9080", varibaleGroup + "/productpage:mono" ]) 
