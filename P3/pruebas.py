from asyncio.windows_events import NULL
from bottle import post, response, request, run, get, route
import json
import datetime

with open ("userDB.json") as j: 
        database = json.load(j)

Idsala = "E01"



print(database['usuarios'][0]['DNI'])

for i in range (0, len(database['usuarios'])):                                        #database es el json que hemos creado donde se almacena todo
        print(database['usuarios'][i]['password'])
