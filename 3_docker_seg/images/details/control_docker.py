from os import environ,path,sys,chdir
from subprocess import call,run
import os
import getpass

# Añadir files necesarios
if not path.exists("./details"):
    call(["cp","-r","../../../practica_creativa2/bookinfo/src/details","./"])

segundo_argumento = ""
if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]


if segundo_argumento == "create":
    # chdir('docker-compose/details')
    chdir('images/details')

varibaleGroup =  environ.get('GRUPO_NUMERO')

# docker build -t 09/productpage
call(["sudo","docker","build","-t", varibaleGroup + "/details","."])

