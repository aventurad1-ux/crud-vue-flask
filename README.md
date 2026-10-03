# CRUD Vue 3 + Axios + Flask

Proyecto desarrollado para el curso de Desarrollo Web (036) de la Universidad Mariano Gálvez.

La aplicación permite administrar clientes, productos y pedidos mediante operaciones CRUD, utilizando Vue 3 en el frontend y Flask en el backend.

## Tecnologías utilizadas

### Backend

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-CORS
- SQLite
- Pytest

### Frontend

- Vue 3
- Vue Router
- Axios
- Vite
- ESLint
- Prettier

## Funcionalidades

La aplicación permite:

- Crear, consultar, actualizar y eliminar clientes.
- Crear, consultar, actualizar y eliminar productos.
- Crear pedidos.
- Consultar pedidos.
- Cambiar el estado de los pedidos.
- Eliminar pedidos cancelados.
- Validar campos obligatorios.
- Validar precios y cantidades.
- Validar stock disponible.
- Evitar correos duplicados.
- Impedir eliminar clientes que tengan pedidos relacionados.
- Impedir eliminar productos que tengan pedidos relacionados.
- Navegar entre las vistas sin recargar completamente la página.
- Consumir una API REST de Flask mediante Axios.

## Estructura del proyecto

~~~text
crud-vue-flask/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── clientes.py
│   │   │   ├── productos.py
│   │   │   └── pedidos.py
│   │   │
│   │   ├── __init__.py
│   │   ├── extensions.py
│   │   ├── models.py
│   │   └── errors.py
│   │
│   ├── migrations/
│   │
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_clientes.py
│   │   └── test_productos.py
│   │
│   ├── .env.example
│   ├── requirements.txt
│   ├── requirements-lock.txt
│   └── run.py
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   ├── http.js
│   │   │   ├── clientes.js
│   │   │   ├── productos.js
│   │   │   └── pedidos.js
│   │   │
│   │   ├── assets/
│   │   │   └── main.css
│   │   │
│   │   ├── components/
│   │   │   ├── AlertMessage.vue
│   │   │   ├── BaseButton.vue
│   │   │   ├── BaseInput.vue
│   │   │   └── DataTable.vue
│   │   │
│   │   ├── router/
│   │   │   └── index.js
│   │   │
│   │   ├── views/
│   │   │   ├── DashboardView.vue
│   │   │   ├── ClientesView.vue
│   │   │   ├── ProductosView.vue
│   │   │   └── PedidosView.vue
│   │   │
│   │   ├── App.vue
│   │   └── main.js
│   │
│   ├── .env.example
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
~~~

## Arquitectura del proyecto

El proyecto está dividido en dos aplicaciones principales: backend y frontend.

### Backend

El backend fue desarrollado con Flask.

La configuración principal de la aplicación se encuentra en:

~~~text
backend/app/__init__.py
~~~

Las extensiones utilizadas por Flask se encuentran en:

~~~text
backend/app/extensions.py
~~~

En este archivo se configuran:

- SQLAlchemy.
- Flask-Migrate.
- Flask-CORS.

Los modelos de la base de datos se encuentran en:

~~~text
backend/app/models.py
~~~

Se utilizan tres entidades principales:

- Cliente.
- Producto.
- Pedido.

La relación permite que un cliente pueda tener pedidos y que un producto pueda estar relacionado con pedidos.

Los endpoints de la API REST se encuentran separados dentro de:

~~~text
backend/app/api/
~~~

Cada recurso tiene su propio archivo:

~~~text
clientes.py
productos.py
pedidos.py
~~~

Las validaciones y respuestas de error comunes se encuentran en:

~~~text
backend/app/errors.py
~~~

Flask-SQLAlchemy se utiliza para trabajar con la base de datos mediante modelos ORM.

Flask-Migrate se utiliza para administrar los cambios y migraciones de la base de datos.

### Frontend

El frontend fue desarrollado con Vue 3.

Las páginas principales se encuentran en:

~~~text
frontend/src/views/
~~~

La aplicación contiene cuatro vistas:

- Dashboard.
- Clientes.
- Productos.
- Pedidos.

Los componentes reutilizables se encuentran en:

~~~text
frontend/src/components/
~~~

Se utilizan los siguientes componentes:

- BaseButton.vue
- BaseInput.vue
- DataTable.vue
- AlertMessage.vue

Estos componentes permiten reutilizar botones, campos de formulario, tablas y mensajes de error.

Las llamadas HTTP están organizadas dentro de:

~~~text
frontend/src/api/
~~~

Axios se utiliza para realizar las solicitudes al backend Flask.

El archivo:

~~~text
frontend/src/api/http.js
~~~

contiene la configuración general de Axios.

Vue Router se utiliza para navegar entre las diferentes vistas sin recargar completamente la página.

## Base de datos

La aplicación utiliza SQLite durante el desarrollo.

Las tablas principales son:

### Clientes

Contiene información como:

- ID.
- Nombre.
- Correo.
- Teléfono.

El correo debe ser único.

### Productos

Contiene información como:

- ID.
- Nombre.
- Descripción.
- Precio.
- Stock.
- Estado activo.

El precio y el stock no pueden tener valores negativos.

### Pedidos

Contiene información como:

- ID.
- Cliente.
- Producto.
- Cantidad.
- Estado.

Los estados disponibles son:

- pendiente
- pagado
- enviado
- cancelado

Cada pedido contiene un solo producto.

## Instalación del backend

Entrar a la carpeta del backend:

~~~powershell
cd backend
~~~

Crear el entorno virtual:

~~~powershell
py -m venv .venv
~~~

Activar el entorno virtual:

~~~powershell
.venv\Scripts\Activate.ps1
~~~

Instalar las dependencias:

~~~powershell
py -m pip install -r requirements.txt
~~~

Ejecutar las migraciones de la base de datos:

~~~powershell
flask --app run.py db upgrade
~~~

Iniciar el servidor Flask:

~~~powershell
flask --app run.py run --debug
~~~

El backend se ejecutará normalmente en:

~~~text
http://localhost:5000
~~~

Para comprobar que el backend está funcionando se puede utilizar:

~~~text
http://localhost:5000/health
~~~

## Instalación del frontend

Desde la carpeta principal del proyecto entrar a:

~~~powershell
cd frontend
~~~

Instalar las dependencias:

~~~powershell
npm install
~~~

Iniciar el servidor de desarrollo:

~~~powershell
npm run dev
~~~

El frontend se ejecutará normalmente en:

~~~text
http://localhost:5173
~~~

## Variables de entorno

El backend contiene el archivo:

~~~text
backend/.env.example
~~~

Este archivo incluye variables como:

~~~text
FLASK_APP
FLASK_DEBUG
DATABASE_URL
FRONTEND_ORIGIN
SECRET_KEY
~~~

El frontend contiene:

~~~text
frontend/.env.example
~~~

con la variable:

~~~text
VITE_API_URL=http://localhost:5000/api
~~~

Los archivos `.env` reales no deben subirse al repositorio porque pueden contener información privada o claves de configuración.

## Rutas del frontend

La aplicación contiene las siguientes rutas:

~~~text
/dashboard
/clientes
/productos
/pedidos
~~~

La ruta principal redirige automáticamente al Dashboard.

## API REST

### Clientes

~~~text
GET    /api/clientes
POST   /api/clientes
GET    /api/clientes/<id>
PUT    /api/clientes/<id>
DELETE /api/clientes/<id>
~~~

### Productos

~~~text
GET    /api/productos
POST   /api/productos
GET    /api/productos/<id>
PUT    /api/productos/<id>
DELETE /api/productos/<id>
~~~

### Pedidos

~~~text
GET    /api/pedidos
POST   /api/pedidos
GET    /api/pedidos/<id>
PUT    /api/pedidos/<id>
DELETE /api/pedidos/<id>
~~~

## Validaciones

La aplicación realiza validaciones tanto en el frontend como en el backend.

Entre las principales validaciones se encuentran:

- Nombre obligatorio para clientes.
- Correo obligatorio para clientes.
- Correos únicos.
- Nombre obligatorio para productos.
- Precio mayor o igual a cero.
- Stock mayor o igual a cero.
- Cliente obligatorio para crear un pedido.
- Producto obligatorio para crear un pedido.
- Cantidad mayor que cero.
- Existencia del cliente y producto seleccionados.
- Verificación de stock disponible.
- Validación de los estados de los pedidos.
- Solo se pueden eliminar pedidos que estén cancelados.

## Pruebas

El backend incluye pruebas automatizadas realizadas con Pytest.

Las pruebas se encuentran en:

~~~text
backend/tests/
~~~

Actualmente se incluyen pruebas para:

- Crear y listar clientes.
- Crear y listar productos.

Para ejecutar las pruebas:

~~~powershell
cd backend
.venv\Scripts\Activate.ps1
py -m pytest
~~~

Si las pruebas son correctas se mostrará un resultado similar a:

~~~text
2 passed
~~~

## Ejecución del proyecto

Para utilizar la aplicación se deben mantener dos terminales abiertas.

### Terminal 1 - Backend

~~~powershell
cd backend
.venv\Scripts\Activate.ps1
flask --app run.py run --debug
~~~

### Terminal 2 - Frontend

~~~powershell
cd frontend
npm run dev
~~~

Después abrir en el navegador:

~~~text
http://localhost:5173
~~~

## Explicación breve del proyecto

La aplicación utiliza una arquitectura separada entre frontend y backend.

Flask funciona como una API REST encargada de manejar los datos, validaciones, modelos y operaciones de la base de datos.

Vue 3 se encarga de presentar la interfaz gráfica al usuario.

Axios permite la comunicación entre Vue y Flask mediante solicitudes HTTP.

Vue Router administra la navegación entre Dashboard, Clientes, Productos y Pedidos.

SQLAlchemy permite trabajar con la base de datos utilizando modelos de Python, mientras que Flask-Migrate administra las migraciones.

Esta separación permite mantener el proyecto organizado y facilita su mantenimiento y ampliación.

## Autor

Proyecto académico desarrollado para el curso Desarrollo Web (036) de la Universidad Mariano Gálvez.