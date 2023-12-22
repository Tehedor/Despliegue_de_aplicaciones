from os import environ,path,sys,chdir
from subprocess import call,run
import os
import getpass

segundo_argumento = ""
if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]


if segundo_argumento == "create":
    chdir('docker-compose/productPage_mono')

varibaleGroup =  environ.get('GRUPO_NUMERO')

call(["cp","-r","../../practica_creativa2/bookinfo/src/productpage","."])


call(["sudo","docker","build","-t",varibaleGroup + "/productpage:mono" ,"."])
   
