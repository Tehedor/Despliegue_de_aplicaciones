from subprocess import call
from os import sys

segundo_argumento = ""

if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]

################  Help  ################
if segundo_argumento == "-h" or segundo_argumento == "--help":
    print("""
    Uso:    control_chart.py [opcion] 
    opcion:
        " " (vacío)     -> Instalar charts (deployments y services)
        eliminar_todo   -> Eliminar charts (deployments y services)
        add_repo        -> Añadir repo de helm

    """)
    exit(0)
    

# ######################################################################################################################
# Añadir repo de helm
# ######################################################################################################################
if segundo_argumento == "add_repo":
    call(["helm","repo","add","stehedor","https://tehedor.github.io/helmcharts/"])
    exit(0)

# ######################################################################################################################
# Eliminar charts (deployments y services)
# ######################################################################################################################
if segundo_argumento == "eliminar_todo":
    call(["helm", "uninstall", "details"])
    call(["helm", "uninstall", "productpage"])
    call(["helm", "uninstall", "ratings"])
    call(["helm", "uninstall", "reviews"])
    exit(0)

# ######################################################################################################################
# Instalar charts (deployments y services)
# ######################################################################################################################
call(["helm", "install" , "details", "stehedor/details"])
call(["helm", "install" , "productpage", "stehedor/productpage"])
call(["helm", "install" , "ratings", "stehedor/ratings"])
call(["helm", "install" , "reviews", "stehedor/reviews"])

# ######################################################################################################################
# Otros comandos
# ######################################################################################################################
# helm search repo
# helm ls
