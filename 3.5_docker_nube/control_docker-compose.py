from os import environ,path,sys
from subprocess import call,run
import os
import getpass


segundo_argumento = ""
if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]


if segundo_argumento == "eliminar_contendores":

    # Get the IDs of all containers
    container_ids = check_output(["sudo", "docker", "ps", "-a", "-q"])

    # Remove all containers
    if container_ids:
        for id in container_ids.split():
            call(["sudo", "docker", "stop", id])
            call(["sudo", "docker", "rm", id])

    exit(0)


if segundo_argumento == "eliminar_todo":

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


call(["python3","env.py"])

call(["sudo","docker-compose","up","-d"])

print("export SERVICE_VERSION=" + environ.get('SERVICE_VERSION'))