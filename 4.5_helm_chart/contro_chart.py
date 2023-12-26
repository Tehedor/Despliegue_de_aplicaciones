from subprocess import call

# helm repo add stehedor https://tehedor.github.io/helmcharts/
call(["helm","repo","add","stehedor","https://tehedor.github.io/helmcharts/"])


call(["helm", "install" , "helm_details", "stehedor/details"])
call(["helm", "install" , "helm_productpage", "stehedor/productpage"])
call(["helm", "install" , "helm_ratings", "stehedor/ratings"])
call(["helm", "install" , "helm_reviews", "stehedor/reviews"])