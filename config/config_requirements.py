from os import environ,path,sys
from subprocess import call,run
import os

call(["cp","../practica_creativa2/bookinfo/src/productpage/requirements.txt","../practica_creativa2/bookinfo/src/productpage/requirements_copia.txt"])
copia = open("../practica_creativa2/bookinfo/src/productpage/requirements_copia.txt","r")
file = open("../practica_creativa2/bookinfo/src/productpage/requirements.txt" ,"w")

end = 1
for line in copia:
    # if line.startswith("urllib3"):
    #     file.write("urllib3==1.24.3\n")
    if line.startswith("urllib3"):
        file.write("urllib3==1.21.1\n")
    elif line.startswith("gevent"):
        file.write("gevent==23.9.1\n")
    elif line.startswith("greenlet"):
        file.write("greenlet==3.0.2\n")
    elif line.startswith("testresources"):
        file.write("testresources==2.0.1\n")
        end = 0
    else:
        file.write(line)

if end:
    file.write("testresources==2.0.1\n")

file.close()
copia.close()
call(["rm","../practica_creativa2/bookinfo/src/productpage/requirements_copia.txt"])