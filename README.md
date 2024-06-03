[![Tripleten](https://id.tripleten.com/resources/2jrb4/login/practicum-keycloakify/build/favicon-32x32.png)]()
# Crear kit de productos en Urban Grocers
## Sprint 7
### Grupo 10
#### Por: Morella Jiménez 

## Descripción del proyecto
Este proyecto se desarrollo para probar la aplicación Urban Grocers, de forma automatizada, específicamente el módulo de crear kit de productos.
Se han creado varias listas de comprobación, una de ellas es para el campo ```name``` en la solicitud de creación de un kit de productos, este es el campo que prueba este código.

## Requisitos

- python3
- librerias 
  - request
  - pytest
- Ajustes en configuration.py
  - URL_SERVICE debe tener una url valida

## Archivos

- configuration.py: aquí se almacena la URL del servidor y  las rutas para crear un usuario y para crear un kit.
- data.py: aquí se almacenan los datos de solicitud, como los headers, user body y kit body.
- sender_stand_request.py: aquí se almacena la importación de datos, como la función para crear un nuevo usuario y la función para nombrar los kits.
- create_kit_name_kit_test.py: aquí se almacenan las funciones para las validaciones positivas y negativas, así como las funciones de los casos de prueba. 

## Automatización de pruebas
```sh
pytest .\create_kit_name_kit_test.py
```

### Casos de prueba 


| ID | Description  | ER:                     | Status |
|----|--------------|-------------------------|--------|
| 1	 | El número permitido de caracteres (1): kit_body = { "name": "a"}| 	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud | Aprobada |
| 2	 | El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}| Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud | Aprobada |
| 3	 | El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }| Código de respuesta: 400 | No Aprobada |
| 4	 |El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }| 	Código de respuesta: 400 | No Aproada |
| 5	 |Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }| Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud | Aprobada |
| 6	 |Se permiten espacios: kit_body = { "name": " A Aaa " }| Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud | Aprobada |
| 7	 |Se permiten números: kit_body = { "name": "123" }| Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud | Aprobada |
| 8	 |El parámetro no se pasa en la solicitud: kit_body = { }| Código de respuesta: 400| No Aprobada |
| 9	 |Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }| 	Código de respuesta: 400 | No Aprobada |
