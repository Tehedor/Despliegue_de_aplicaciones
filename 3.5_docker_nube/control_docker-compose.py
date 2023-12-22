from os import environ,path,sys
from subprocess import call,run
import os
import getpass

varibaleGroup =  environ.get('GRUPO_NUMERO')

call(["python3","control_env.py"])

call(["sudo","docker-compose","up","-d"])

# call(["sudo","docker-compose","up","-d"])
