from os import environ,path,sys,chdir
from subprocess import call,run,check_output

segundo_argumento = ""

if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]

if segundo_argumento == "elminar_pods":
    call(["kubectl", "delete", "pods", "--all"])
    exit(0)

# Maquina pesada
call(["kubectl","apply","-f","details.yaml"])
call(["kubectl","apply","-f","productpage.yaml"])
call(["kubectl","apply","-f","reviews-svc.yaml"])
call(["kubectl","apply","-f","reviews-v1-deployment.yaml"])
call(["kubectl","apply","-f","reviews-v2-deployment.yaml"])
call(["kubectl","apply","-f","reviews-v3-deployment.yaml"])
