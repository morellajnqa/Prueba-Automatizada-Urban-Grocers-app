import configuration
import requests
import json
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)

print(response.status_code)
print(data.headers)

if response.status_code == 201:
    authToken= response.json()['authToken']
    print('El token que obtuve fue: '+authToken)
    #agregamos un authorization al header
    data.headers['Authorization'] = 'Bearer ' + authToken
else:
    print(response.json())

def post_kits(name):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=name,
                         headers=data.headers)

response = post_kits(data.kit_body);
print(response.status_code)
print(response.json())