import requests
print('Bienvenido a...')
response = requests.get('http://localhost:8080/ListCourses')
print(response.status_code)
print(response.text)