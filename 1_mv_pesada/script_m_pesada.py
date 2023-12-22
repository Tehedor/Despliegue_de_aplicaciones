from os import environ,path,sys
from subprocess import call,run
import os

segundo_argumento = ""
if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]


chdir("1_mv_pesada/productpage")

if segundo_argumento == "configurar":
    call(["pip3","install","-r","requirements.txt"])
    sys.exit(0)
    
call(["python3","productpage_monolith.py","9080"])

