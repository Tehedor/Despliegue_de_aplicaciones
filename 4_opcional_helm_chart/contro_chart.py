from subprocess import call
from os import sys

segundo_argumento = ""

if not len(sys.argv) < 2:
    segundo_argumento = sys.argv[1]

if segundo_argumento == "add_repo":
    call(["helm","repo","add","stehedor","https://tehedor.github.io/helmcharts/"])
    exit(0)

if segundo_argumento == "eliminar_todo":
    call(["helm", "uninstall", "details"])
    call(["helm", "uninstall", "productpage"])
    call(["helm", "uninstall", "ratings"])
    call(["helm", "uninstall", "reviews"])
    exit(0)

call(["helm", "install" , "details", "stehedor/details"])
call(["helm", "install" , "productpage", "stehedor/productpage"])
call(["helm", "install" , "ratings", "stehedor/ratings"])
call(["helm", "install" , "reviews", "stehedor/reviews"])
