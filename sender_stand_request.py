import configuration
import requests
import data
import copy

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def get_auth_header ():
    response = post_new_user(data.user_body)
    if response.status_code == 201:
        auth_header = copy.copy(data.headers)
        auth_header['Authorization'] = 'Bearer ' + response.json()['authToken']
        return auth_header
    else:
        return response
def post_kits(name, auth_headers=data.headers):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=name,
                         headers=auth_headers)
