from re import I
from bottle import  route, run, request, response, get, post, put
import json





@route('/login') # o @route('/login', method='POST')                      

def do_login():
    
    username = "userSD"
    password = "passwordSD45"

    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


def check_login(username, password):
    encontrado = 0

    with open('userDB.json') as file:
        data = json.load(file)

    for usuario in data['usuarios']:
        if username == usuario["userName"] and password == usuario["password"]:
            encontrado = 1
            break
    return encontrado

run(host='localhost', port=8088)


@route('/MostrarSala')




class sala:
    def __init__(self, id, capacidad, recursos):
        self.id = id
        self.capacidad = capacidad
        self.recursos = recursos



@post('/AñadirSala')
def añadir_sala():
    #import pdb; pdb.set_trace()
    with open('userBD.json') as file:
        data = json.load(file)
    # Datos del JSON
    id = data.get('id')
    capacidad = data.get('capacidad')
    recursos = data.get('recursos')
    recursos = sala(id, capacidad, recursos)

    # persistencia (tendríamos que implementar los métodos de conexión con la base de datos etc.)
    # save_data(course)
    # Añadimos instancia a nuestra base de datos

    #database[id] = sala

    # Una vez almacenada la instancia, es conveniente devolver una respuesta al usuario
    # Construimos la cabecera: 'application/json' indicamos que vamos a devolver un JSON

    response.headers['Content-Type'] = 'application/json'
    dict_to_parse = {'id': id, 'capacidad': capacidad, 'recursos': recursos}
    # Devolvemos el JSON
    return json.dumps(dict_to_parse)

