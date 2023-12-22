from os import environ,path,sys
from subprocess import call,run,check_output
import os
import getpass

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


if segundo_argumento == "resetear_contendores":

    # Get the IDs of all containers
    container_ids = check_output(["sudo", "docker", "ps", "-a", "-q"])

    # Remove all containers
    if container_ids:
        for id in container_ids.split():
            call(["sudo", "docker", "stop", id])
            call(["sudo", "docker", "rm", id])

    exit(0)

if segundo_argumento == "images":
    call(["python3","images/details/control_docker.py","create"])
    call(["python3","images/productPage_seg/control_docker.py","create"])
    call(["python3","images/ratings/control_docker.py","create"])
    exit(0)

if segundo_argumento == "reviews":
    call(["python3","images/reviews/control_docker.py","create"])
    exit(0)

if segundo_argumento == "resetear_todo":

    # Get the IDs of all containers
    container_ids = check_output(["sudo", "docker", "ps", "-a", "-q"])

    # Remove all containers
    if container_ids:
        for id in container_ids.split():
            call(["sudo", "docker", "stop", id])
            call(["sudo", "docker", "rm", id])

    images_ids = check_output(["sudo", "docker", "images", "-q"])

    # Remove all images
    if images_ids:
        for id in images_ids.split():
            call(["sudo", "docker", "rmi","-f", id])

    # Remove all volumes

    images_names = check_output(["sudo", "docker", "volume", "ls","-q"])

    # Remove all containers
    if images_ids:
        for id in images_names.split():
            call(["sudo", "docker", "volume","rm", id])

    exit(0)

call(["python3","control_env.py"])

call(["sudo","docker-compose","up","-d"])

# call(["sudo","docker-compose","up","-d"])
print("export GRUPO_NUMERO=" + environ.get('GRUPO_NUMERO'))