from os import environ

# environ['GRUPO_NUMERO'] = '09'
# environ['SERVICE_VERSION'] = 'v1'
# environ['ENABLE_EXTERNAL_BOOK_SERVICE'] = 'true'

varibaleGroup =  str(environ.get('GRUPO_NUMERO'))
serviceVersion =  str(environ.get('SERVICE_VERSION'))

print("\nGRUPO_NUMERO=" + varibaleGroup + "         -> export GRUPO_NUMERO=09\n")
print("SERVICE_VERSION=",serviceVersion + "        -> export SERVICE_VERSION=v1 \n")
print("export SERVICE_VERSION=v1 export GRUPO_NUMERO=09 \n")

# export GRUPO_NUMERO="09"
# export SERVICE_VERSION="v1"
# export ENABLE_EXTERNAL_BOOK_SERVICE=true
# GRUPO_NUMERO 09
# SERVICE_VERSION v1
# ENABLE_EXTERNAL_BOOK_SERVICE True




