# 1 - Agente asistente de ventas - Extraccion e inserccion de datos en BD.
# 1. pipeline ETL

-   Generación de datos sintéticos, e inserccion en Base de datos.

-   Python, Faker, sqlalchemy, psycopg2, pandas, Base de datos PostgreSQL (Supabase).

-   Modelo de BD:

   <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_01_etl_preprocesamiento/blob/main/images/bd.png" alt="logo" />
   </div>
---

# 2. Implementación

-   Extracción: generación de datos con Faker.

-   Transformación: limpieza de datos para que no haya datos repetidos (clave email).

-   Generación: datos a ficheros csv.

-   Carga de datos: Se crean las tablas de base de datos y se almacena la información.
---
# 3. Proceso

-   Genera un DataFrame simulado con datos de alumnos utilizando la biblioteca Faker, con columnas: 
    nombre, apellidos, email, estudios, especialidad, ciudad, edad, teléfono, sexo y motivo de compra.

-   Genera un DataFrame simulado con datos de leads utilizando la biblioteca Faker, con columnas: 
    nombre, apellidos, email, estudios, especialidad, ciudad, edad, teléfono, sexo y motivo de compra.

-   Elimina duplicados entre los DataFrames de leads y alumnos basándose en la columna 'email'.

-   Guarda los DataFrames de leads y alumnos en archivos CSV con pandas, test de datos insertados con psycopg2.

-   Creación e inserción de datos con sqlalchemy en las tablas 'alumnos' y 'leads' en una base de datos de PostgreSQL.
---
## Requisitos del Entorno

Para asegurar la correcta ejecución del proyecto, es necesario instalar las siguientes dependencias en un entorno virtual de Python:

- **pandas**: Para manipulación y análisis de datos.
- **numpy**: Para operaciones numéricas.
- **Faker**: Para generación dataset sinteticos.
- **SQLAlchemy**: Creacion/inserccion de datos en BD.
- **psycopg2**: psycopg2 - Python-PostgreSQL Database Adapter.

---
# Proyecto
   <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_01_etl_preprocesamiento/blob/main/images/estructura.png" alt="logo" />
   </div>
---

## Configuración del Entorno

Sigue estos pasos para configurar el entorno de desarrollo:

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/santiagorodriguez-dev/pf_01_etl_preprocesamiento.git
cd pf_01_etl_preprocesamiento
```

### 2️⃣ Crear y activar un entorno virtual

```bash
python -m venv venv
```

#### En Windows:
```bash
venv\Scripts\activate
```

#### En macOS/Linux:
```bash
source venv/bin/activate
```

### 3️⃣ Instalar las dependencias

```bash
pip install -r requirements.txt
```
---
# Notas
-   Para la ejecucion del notebook, crear fichero .env en el raiz del proyecto.

```sh
DB_USER='user'
DB_PASSWORD='pass'
ACCOUNT_IDENTIFIER='url_identificador'
DB_NAME='Nombre_base_de_datos'
```
---
# 4. Ejecucion
```sh
  D:\workspace\pf_01_etl_preprocesamiento>python main.py
  Inicio creacion de dataset
  Numero de df_leads:  95
  Numero de df_alumnos:  29533
  Conexión realizada con éxito
  Resultados en la tabla alumnos: 29533
  Resultados en la tabla leads: 95
```

## Licencia

Este proyecto está licenciado bajo la Licencia Apache 2.0. Para más detalles, consulta el archivo [LICENSE](LICENSE).

---

## Autores
* **Santiago Rodriguez** - [santiagorodriguez-dev](https://github.com/santiagorodriguez-dev)
