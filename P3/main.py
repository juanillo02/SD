"""
from bottle import route, run       #Escribir hola mundo
@route('/hello')
def hello():
 return "Hello World!"
run(host='localhost', port=8080, debug=True)
"""
"""
# Ejemplo: Hello World              #Escribir un nombre
from bottle import route, run, template
@route('/hello/<name>')
def index(name):
 return template('<b> Hello {{name}} </b>!', name=name)
run(host='localhost', port=8081)
"""
"""
#Ejemplo: router                    #Router
from bottle import route, run, template
@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
 return template('<b> Hello {{name}}, how are you?', name=name)
run(host='localhost', port=8082)
"""
"""
#Se pueden definir parámetros entre <>.
#Se puede indicar el tipo del parámetro :int o :float.
#Se pueden incluir expresiones regulares con :re.
from bottle import route, run, template
@route('/')
@route('/object/<id:int>')
def callback(id):
 assert isinstance(id, int)

@route('/show/<name:re:[a-z]+>')
def callback(name):
 assert name.isalpha()
 """
"""
#Request (GET)
from bottle import get, run # request o route
@get('/cars') # o @route('/cars')
def getcars():
 cars = [ {'name': 'Audi', 'price': 52642},
 {'name': 'Mercedes', 'price': 57127},
 {'name': 'Skoda', 'price': 9000},
 {'name': 'Volvo', 'price': 29000},
 {'name': 'Bentley', 'price': 350000},
 {'name': 'Citroen', 'price': 21000},
 {'name': 'Hummer', 'price': 41400},
 {'name': 'Volkswagen', 'price': 21600} ]
 return dict(data=cars)
run(host='localhost', port=8088)
"""
"""
#Request (POST)                #NO VA
from bottle import post, request # o route
@post('/login') # o @route('/login', method='POST')
def do_login():
 try:
    data = request.json()
 except:
    raise ValueError
 if data is None:
    raise ValueError
 username = data['username']
 password = data['password']
 if check_login(username, password):
    return "<p>Your login information was correct.</p>"
 else:
    return "<p>Login failed.</p>"
"""
"""
#Request (PUT)
import json
from bottle import put, request, response, run # o route
_names=["Sara"]
# o @route('/names/<oldname>', method='PUT')
@put('/names/<oldname>')
def update_handler(oldname):
    try:
        data = json.load((request.body))
    except:
        raise ValueError
    newname = data['name']
    _names.remove(oldname)
    _names.append(newname)
    # return 200 Success
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'name': newname})
run(host='localhost', port=8084)
"""

#Ejemplo de prácticas: parte del servidor
import json
from bottle import run, request, response, get, post, put
# Simulamos base de datos en memoria
database = dict() #key: code, value: course
# Creamos una clase Course (Curso) con un constructor que tiene: nombre y
# código de asignatura, que inicializamos
class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name

#Ejemplo de prácticas: crear una asignatura
@post('/AddCourse')
def add_course():
    #import pdb; pdb.set_trace()
    data = request.json
    # Datos del JSON
    code = data.get('code')
    name = data.get('name')
    course = Course(code, name)
    # persistencia (tendríamos que implementar los métodos de conexión con la base de datos etc.)
    # save_data(course)
    # Añadimos instancia a nuestra base de datos
    database[code] = course
    # Una vez almacenada la instancia, es conveniente devolver una respuesta al usuario
    # Construimos la cabecera: 'application/json' indicamos que vamos a devolver un JSON
    response.headers['Content-Type'] = 'application/json'
    dict_to_parse = {'code': code, 'name': name}
    # Devolvemos el JSON
    return json.dumps(dict_to_parse)
#Ejemplo de prácticas: consultar lista de asignaturas
@get('/ListCourses')
def list_asignaturas():
    asignaturas = []
    for key, value in database.items():
        asignaturas.append({'code': key, "name": value.name})
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(asignaturas)
#Ejemplo de prácticas: actualizar una asignatura
@put('/UpdateCourse/<course_code>')
def update_course(course_code):
    # Suponemos que la asignatura está en la base de datos
    course = database[course_code]
    response.headers[ 'Content-Type'] = 'application/json'
    new_name = request.json.get( 'name')
    course.name = new_name
    dict_to_parse = { 'code': course_code, 'name': course.name}
    # Devolvemos el JSON
    return json.dumps(dict_to_parse)
#Ejemplo de prácticas:
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
"""
#Ejemplo de prácticas: parte del cliente
import requests
print('Bienvenido a...')
response = requests.get('http://localhost:8080/ListCourses')
print(response.status_code)
print(response.text)
"""
