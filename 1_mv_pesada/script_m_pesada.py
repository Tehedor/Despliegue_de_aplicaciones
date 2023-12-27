from os import environ,path,sys,chdir
from subprocess import call,run
import os


if not path.exists("./productpage"):
     call(["cp","-r","../practica_creativa2/bookinfo/src/productpage","."])

segundo_argumento = ""
if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]

################  Help  ################
if segundo_argumento == "-h" or segundo_argumento == "--help":
    print("""
        ((( Ojo ))) 
            Variable de entorno: GRUPO_NUMERO
            -> export GRUPO_NUMERO=09

    Uso:    scritps_m_pesada.py [opcion] 
    opcion:
        " " (vacío)     -> Arrancar en el puerto 9080
        configurar      -> Instalar dependencias de python
    """)
    exit(0)


# Directorio productpage
chdir("productpage")

# ######################################################################################################################
# Instalar en la mv las dependencias de python necesarias
# ######################################################################################################################
if segundo_argumento == "configurar":
    call(["pip3","install","-r","requirements.txt"])
    sys.exit(0)
    
# ######################################################################################################################
# Ejecutar aplicaion en el puerto 9080
# ######################################################################################################################
call(["python3","productpage_monolith.py","9080"])
