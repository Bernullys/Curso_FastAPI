Creating our first app
    Using a venv

Automatic documentation with Swagger
    add to the url: /docs

Methods:

GET

    Parametros de ruta
        Como se reciben parametros por la ruta y como se filtran por id

    Parametros Query
        Son una serie de clave valor para realizar busquedas. Tenia un error de sintaxis.

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
    Parametros query:
        importar Query
    
Tipos de respuestas:
    importar JSONResponse

    Modelo de respuesta que vamos a obtener:
        importar List

Codigos de estados


Flujo de autenticación:
    Ruta para iniciar sesión:
        Lo que obtendremos como resultado al final de este módulo es la protección de determinadas rutas de nuestra aplicación para las cuales solo se podrá acceder mediante el inicio de sesión del usuario. Para esto crearemos una ruta que utilice el método POST donde se solicitarán los datos como email y contraseña.
    Creación y envío de token:
        Luego de que el usuario ingrese sus datos de sesión correctos este obtendrá un token que le servirá para enviarlo al momento de hacer una petición a una ruta protegida.
    Validación de token:
        Al momento de que nuestra API reciba la pteción del usuario, comprobará que este le haya enviado el token y validará si es correcto y le pertenece. Finalmente se le dará acceso a la ruta que está solicitando.

    Generando tokens con pyjwt
