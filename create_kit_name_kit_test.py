import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    auth_header = sender_stand_request.get_auth_header()
    kit_body = get_kit_body(name)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    kit_response = sender_stand_request.post_kits(kit_body,auth_header)
    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == name

def negative_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    auth_header = sender_stand_request.get_auth_header()
    kit_body = get_kit_body(name)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    kit_response = sender_stand_request.post_kits(kit_body,auth_header)
    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 400
    assert kit_response.json()['message'] == "No paso esta validacion"

def negative_assert2(kit_body):
    auth_header = sender_stand_request.get_auth_header()
    kit_response = sender_stand_request.post_kits(kit_body,auth_header)
    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 400
    assert kit_response.json()['message'] == "No paso esta validacion"


def test_kit_body_el_numero_permitido_de_caracteres_1():
    #lista de comprobacion caso 1
    positive_assert('1')

def test_kit_body_el_numero_permitido_de_caracteres_511():
    #lista de comprobacion caso 2
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_kit_body_el_numero_permitido_de_caracteres_0():
    #lista de comprobacion caso 3
    negative_assert("")
def test_kit_body_el_numero_permitido_de_caracteres_512():
    #lista de comprobacion caso 4
    negative_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')

def test_kit_body_se_permiten_caracteres_especiales():
    #lista de comprobacion caso 5
    positive_assert('"№%@",')

def test_kit_body_se_permiten_espacios():
    #lista de comprobacion caso 6
    positive_assert('A aaa')

def test_kit_body_se_permiten_numeros():
    #lista de comprobacion caso 7
    positive_assert('1234')

def test_kit_body_el_parametro_no_se_pasa_en_la_solicitud():
    #lista de comprobacion caso 8
    negative_assert2({ })
def test_kit_body_se_ha_pasado_un_tipo_de_parámetro_diferente_numero():
    #lista de comprobacion caso 9
    negative_assert(123)