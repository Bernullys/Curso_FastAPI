Creating our first app
    Using a venv

Automatic documentation with Swagger
    add to the url: /docs

Methods:

GET

    Parametros de ruta
        Como se reciben parametros por la ruta y como se filtran por id

    Parametros Query
        Son una serie de clave valor para realizar busquedas

POST
PUT
DELETE

Esquemas:
    Se utilizan con la libreria pydantic, para tener una clase con los keys y no pasarselos directamente a los parametros de las fuciones.

Validación de datos:
    Para que los datos introducidos cumplan con el tipo.
    FastAPI genera algunas validaciones automaticamente (como tipo de dato).
    Para agregar otras se importa Field

    gt: greater than
    ge: greater than or equal
    lt: less than
    le: less than or equal

Validación de Parametros:
    Parametros de ruta:
        importar Path

    

