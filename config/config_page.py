from os import environ,path,sys
from subprocess import call,run
import os


varibaleGroup =  'GRUPO_'  + environ.get('GRUPO_NUMERO')
print(varibaleGroup)

# Editar fichero productpage.py

call(["cp","../practica_creativa2/bookinfo/src/productpage/templates/productpage.html","../practica_creativa2/bookinfo/src/productpage/templates/productpage_copy.html"])
copia = open(",./practica_creativa2/bookinfo/src/productpage/templates/productpage_copy.html","r")
file = open("../practica_creativa2/bookinfo/src/productpage/templates/productpage.html" ,"w")

for line in copia:
    if line.startswith('{% block title %}'):
        file.write("{% block title %} " +  varibaleGroup + "{% endblock %}\n")
    else:
        file.write(line)

file.close()
copia.close()
call(["rm","../practica_creativa2/bookinfo/src/productpage/templates/productpage_copy.html"])