from os import environ,path,sys
from subprocess import call,run
import os
import getpass


call(["python3","control_env.py"])

call(["sudo","docker-compose","up","-d"])

print("export GRUPO_NUMERO=" + environ.get('GRUPO_NUMERO'))