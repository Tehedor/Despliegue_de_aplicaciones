from os import environ,path,sys,chdir
from subprocess import call,run,check_output

varibaleGroup =  environ.get('GRUPO_NUMERO')
serviceVersion = environ.get('SERVICE_VERSION')


if not varibaleGroup:
    print("No se ha definido la variable de entorno GRUPO_NUMERO")
    sys.exit(1)

if not serviceVersion:
    print("No se ha definido la variable de entorno SERVICE_VERSION")
    sys.exit(1)

if not path.exists("./practica_creativa2"):
    # Instalar y actualizar todo lo necesario para que funcione la practica
    call(["sudo","apt-get","update"])
    call(["sudo","apt-get","install","python3","-y"])
    call(["sudo","apt-get","install","python3-pip","-y"])
    call(["sudo","apt-get","install","docker.io","-y"])
    call(["sudo","apt-get","install","docker-compose","-y"])
    
    # Configurar todo el directorio para que funcione de manera adecuda toda la practica
    call(["git","clone","https://github.com/CDPS-ETSIT/practica_creativa2.git"])
    call(["python3","config/config_requirements.py"])
    call(["python3","config/config_page.py"])
