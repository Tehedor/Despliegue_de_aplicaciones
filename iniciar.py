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
    # # call(["pip3","install","-r","./practica_creativa2/bookinfo/src/productpage/requirements.txt"])


    # 1_mv_pesada
    # call(["cp","-r","./practica_creativa2/bookinfo/src/productpage","./1_mv_pesada/"])

    # 2_docker_mono
    # call(["cp","-r","./practica_creativa2/bookinfo/src/productpage","./2_docker_mono/productPage_mono/"])

    # 3_docker_seg
    # call(["cp","-r","./practica_creativa2/bookinfo/src/details","./3_docker_seg/images/details/"])
    # call(["cp","-r","./practica_creativa2/bookinfo/src/productpage","./3_docker_seg/images/productPage_seg/"])
    # call(["cp","-r","./practica_creativa2/bookinfo/src/ratings","./3_docker_seg/images/ratings/"])
    # call(["cp","-r","./practica_creativa2/bookinfo/src/reviews","./3_docker_seg/images/reviews/"])
    # call(["cp","-r","./practica_creativa2/bookinfo/src/productpage","./1_mv_pesada"])


