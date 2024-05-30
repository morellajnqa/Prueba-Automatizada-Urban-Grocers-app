[![Tripleten](https://id.tripleten.com/resources/2jrb4/login/practicum-keycloakify/build/favicon-32x32.png)]()
# Proyecto Urban Grocers 
###### Por: Morella Jiménez 

## Proyecto para el séptimo sprint: Tarea
Se han creado varias listas de comprobación,
una de ellas es para el campo ```name``` en la solicitud de creación de un kit de productos.

### Lista de comprobación de pruebas 


| №  | Description  | ER:                     | Status | Error |
|----|--------------|-------------------------|--------|-------|
|1	| El número permitido de caracteres (1): kit_body = { "name": "a"}| 	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud | Aprobada |
|2	| El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}| Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud |
|3	| El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }| Código de respuesta: 400 |
|4	|El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }| 	Código de respuesta: 400 |
|5	|Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }| Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
|6	|Se permiten espacios: kit_body = { "name": " A Aaa " }| Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
|7	|Se permiten números: kit_body = { "name": "123" }| Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
|8	|El parámetro no se pasa en la solicitud: kit_body = { }| Código de respuesta: 400|
|9	|Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }| 	Código de respuesta: 400 |

# Requisitos

- pyton3
- librerias 
  - request
  - pytest
- Ajustes en configuration.py
  - URL_SERVICE debe tener una url valida

## correr todos los casos de pruebas
```sh
pytest .\create_kit_name_kit_test.py
```
