from subprocess import call
from os import sys
# helm repo add stehedor https://tehedor.github.io/helmcharts/

segundo_argumento = ""

if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]

if segundo_argumento == "add_repo":
    call(["helm","repo","add","stehedor","https://tehedor.github.io/helmcharts/"])
    exit(0)

if segundo_argumento == "eliminar_todo":
    call(["helm", "uninstall", "helmDetails"])
    call(["helm", "uninstall", "helmProductpage"])
    call(["helm", "uninstall", "helmRatings"])
    call(["helm", "uninstall", "helmReviews"])


    exit(0)



call(["helm", "install" , "helmDetails", "stehedor/details"])
call(["helm", "install" , "helmProductpage", "stehedor/productpage"])
call(["helm", "install" , "helmRatings", "stehedor/ratings"])
call(["helm", "install" , "helmReviews", "stehedor/reviews"])
