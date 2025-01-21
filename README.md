# 1. pipeline ETL

-   Genereacion de datos sinteticos, guardado en csv y Base de datos.

-   Python, Faker, sqlalchemy, psycopg2, pandas, Base de datos PostgreSQL (Supabase).

-   Modelo de BD:

   <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_01_etl_preprocesamiento/blob/main/images/bd.png" alt="logo" />
   </div>

# 2. Implementación

-   Extracción: Generacion de datos con Faker.

-   Transformación: limpieza de datos para que no haya datos repetidos (clave email).

-   Generación: datos a ficheros csv.

-   Carga de datos: Se crean las tablas de base de datos y se almacena la informacion.

# 3. Proceso

-   Genera un DataFrame simulado con datos de alumnos utilizando la biblioteca Faker, con columnas:
    nombre, apellidos, email, estudios, especialidad, ciudad, edad, teléfono, sexo y motivo de compra.

-   Genera un DataFrame simulado con datos de leads utilizando la biblioteca Faker, con columnas:
    nombre, apellidos, email, estudios, especialidad, ciudad, edad, teléfono, sexo y motivo de compra.

-   Elimina duplicados entre los DataFrames de leads y alumnos basándose en la columna 'email'.

-   Guarda los DataFrames de leads y alumnos en archivos CSV.

-   Creaion e inserccion de datos en las tablas 'alumnos' y 'leads' en una base de datos de PostgreSQL.

