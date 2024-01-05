from os import environ,path,sys,chdir
from subprocess import call,run
import os
import getpass
    
segundo_argumento = ""
if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]


if segundo_argumento == "create":
    chdir('images/productPage_seg')

# Añadir files necesarios
if not path.exists("./productpage"):
    call(["cp","-r","../../../practica_creativa2/bookinfo/src/productpage","./"])

varibaleGroup =  environ.get('GRUPO_NUMERO')

call(["sudo","docker","build","-t",varibaleGroup + "/productpage:seg" ,"."])
   
