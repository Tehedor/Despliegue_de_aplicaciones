from os import environ,path,sys,getcwd,chdir
from subprocess import call,run
import os
import getpass

varibaleGroup =  str(environ.get('GRUPO_NUMERO'))
serviceVersion =  environ.get('SERVICE_VERSION','v1')
with open('.env', 'w') as file:
    file.write("GRUPO_NUMERO=" + varibaleGroup + "\n")
    file.write("SERVICE_VERSION=" + serviceVersion + "\n")
    

file = open(".env", "r")
for linea in file.readlines():
    print(linea)
file.close()

# varibaleGroup =  environ.get('GRUPO_NUMERO')

