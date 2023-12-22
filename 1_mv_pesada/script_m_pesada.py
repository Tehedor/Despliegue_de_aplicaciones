from os import environ,path,sys,chdir
from subprocess import call,run
import os


if not path.exists("./productpage"):
     call(["cp","-r","../practica_creativa2/bookinfo/src/productpage","."])

segundo_argumento = ""
if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]


chdir("productpage")

if segundo_argumento == "configurar":
    call(["pip3","install","-r","requirements.txt"])
    sys.exit(0)
    
call(["python3","productpage_monolith.py","9080"])

