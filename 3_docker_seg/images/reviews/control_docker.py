from os import environ,path,sys,getcwd,chdir
from subprocess import call,run
import os
import getpass

varibaleGroup =  str(environ.get('GRUPO_NUMERO'))

versiones= ["v1","v2","v3"]
colores= ["","black","red"]

segundo_argumento = ""
if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]


if segundo_argumento == "create":
    chdir('images/reviews')
    
if not path.exists("./reviews"):
    call(["cp","-r","../../../practica_creativa2/bookinfo/src/reviews","."])

chdir('reviews/reviews-wlpcfg')

for i,version in enumerate(versiones):
    enableRatings = "true"
    if version == "v1":
        enableRatings = "false"

    starColor = colores[i]
    call(["sudo", "docker", "build", "-t", varibaleGroup + "/reviews:" + version, "--build-arg", "service_version=" + version, "--build-arg", "enable_ratings=" + enableRatings, "--build-arg", "star_color=" + starColor, "."])
    
# call(["sudo", "docker", "build", "-t", varibaleGroup + "/reviews:" + version, "--build-arg", "service_version=" + version, "--build-arg", "enable_ratings=" + enableRatings, "--build-arg", "star_color=" + starColor, "."])
#  sudo docker build -t 09/reviews:v1 --build-arg service_version=v1 .
# call(["sudo","docker","build","-t",varibaleGroup + "/reviews:v1","--build-arg","service_version=v1","."])
