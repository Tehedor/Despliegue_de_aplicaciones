from os import environ,path,sys,chdir
from subprocess import call,run,check_output

segundo_argumento = ""

if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]

################  Help  ################
if segundo_argumento == "-h" or segundo_argumento == "--help":
    print("""
    Uso:    control_kube.py [opcion] 
    opcion:
        " " (vacío)     -> Crear deployments y services
        eliminar_todo   -> Eliminar deployments y services
    """)
    exit(0)

# ######################################################################################################################
# Elimanar deployments y services
# ######################################################################################################################
if segundo_argumento == "eliminar_todo":
    call(["kubectl", "delete", "all", "--all"])
    # call(["kubectl", "delete", "deployment", "--all"])
    # call(["kubectl", "delete", "services", "--all"])
    # call(["kubectl", "stop", "pods", "--all"])
    # call(["kubectl", "delete", "pods", "--all"])
    exit(0)

# ######################################################################################################################
# Crear deployments y services
# ######################################################################################################################
call(["kubectl","apply","-f","details.yaml"])
call(["kubectl","apply","-f","productpage.yaml"])
call(["kubectl","apply","-f","ratings.yaml"])
call(["kubectl","apply","-f","reviews-svc.yaml"])
call(["kubectl","apply","-f","reviews-v1-deployment.yaml"])
call(["kubectl","apply","-f","reviews-v2-deployment.yaml"])
call(["kubectl","apply","-f","reviews-v3-deployment.yaml"])
