# 1. pipeline ETL

-   Generación de datos sintéticos, guardado en csv y Base de datos.

-   Python, Faker, sqlalchemy, psycopg2, pandas, Base de datos PostgreSQL (Supabase).

-   Modelo de BD:

   <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_01_etl_preprocesamiento/blob/main/images/bd.png" alt="logo" />
   </div>

# 2. Implementación

-   Extracción: generación de datos con Faker.

-   Transformación: limpieza de datos para que no haya datos repetidos (clave email).

-   Generación: datos a ficheros csv.

-   Carga de datos: Se crean las tablas de base de datos y se almacena la información.

# 3. Proceso

-   Genera un DataFrame simulado con datos de alumnos utilizando la biblioteca Faker, con columnas: 
    nombre, apellidos, email, estudios, especialidad, ciudad, edad, teléfono, sexo y motivo de compra.

-   Genera un DataFrame simulado con datos de leads utilizando la biblioteca Faker, con columnas: 
    nombre, apellidos, email, estudios, especialidad, ciudad, edad, teléfono, sexo y motivo de compra.

-   Elimina duplicados entre los DataFrames de leads y alumnos basándose en la columna 'email'.

-   Guarda los DataFrames de leads y alumnos en archivos CSV.

-   Creación e inserción de datos en las tablas 'alumnos' y 'leads' en una base de datos de PostgreSQL.

# Proyecto

   <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_01_etl_preprocesamiento/blob/main/images/estructura.png" alt="logo" />
   </div>

# Notas
-   Para la ejecucion del notebook, crear fichero .env en el raiz del proyecto.

```sh
DB_USER='user'
DB_PASSWORD='pass'
ACCOUNT_IDENTIFIER='url_identificador'
DB_NAME='Nombre_base_de_datos'
```

## Construido con 🛠️

* [Pyhton](https://www.python.org/) - Lenguaje utilizado
* [Faker](https://faker.readthedocs.io/en/master/) - Faker
* [sqlalchemy](https://www.sqlalchemy.org/) - sqlalchemy
* [psycopg](https://www.psycopg.org/) - psycopg
* [pandas](https://pandas.pydata.org/docs/) - pandas
* [supabase](https://supabase.com/) - supabase
* [Visual Studio Code](https://code.visualstudio.com/) - IDE desarrollo
  
## Autores ✒️

* **Santiago Rodriguez** - [santiagorodriguez-dev](https://github.com/santiagorodriguez-dev)
