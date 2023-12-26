from subprocess import call

# helm repo add stehedor https://tehedor.github.io/helmcharts/
call(["helm","repo","add","stehedor","https://tehedor.github.io/helmcharts/"])


call(["helm", "install" , "helm", "stehedor/details"])
call(["helm", "install" , "helm", "stehedor/productpage"])
call(["helm", "install" , "helm", "stehedor/ratings"])
call(["helm", "install" , "helm", "stehedor/reviews"])