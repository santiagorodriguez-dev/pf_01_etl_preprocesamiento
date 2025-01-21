import sys
sys.path.append("../")

import os
import dotenv  # type: ignore
dotenv.load_dotenv()

from sqlalchemy import create_engine  # type: ignore
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors  # type: ignore

def create_table_insert(df_alumnos, df_leads):
    """
    Create and insert data into the 'alumnos' and 'leads' tables in a PostgreSQL database.

    Parameters:
        df_alumnos (pandas.DataFrame): DataFrame containing the data to be inserted into the 'alumnos' table.
        df_leads (pandas.DataFrame): DataFrame containing the data to be inserted into the 'leads' table.

    Environment Variables:
        DB_USER (str): Database username.
        DB_PASSWORD (str): Database password.
        DB_NAME (str): Database name.
        ACCOUNT_IDENTIFIER (str): Host identifier for the database.

    Database Operations:
        - Replaces the 'alumnos' table with the data from df_alumnos.
        - Replaces the 'leads' table with the data from df_leads.

    Notes:
        Ensure the environment variables are set correctly before executing this function.
    """
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    ACCOUNT_IDENTIFIER = os.getenv("ACCOUNT_IDENTIFIER")

    user = DB_USER
    password = DB_PASSWORD
    conn_string = f"postgresql+psycopg2://{user}:{password}@{ACCOUNT_IDENTIFIER}:5432/{DB_NAME}"
    engine = create_engine(conn_string)

    # Insert data into 'alumnos' table
    table_name = 'alumnos'
    if_exists = 'replace'
    with engine.connect() as con:
        df_alumnos.to_sql(
            name=table_name.lower(), 
            con=con, 
            if_exists=if_exists
        )

    # Insert data into 'leads' table
    table_name = 'leads'
    if_exists = 'replace'
    with engine.connect() as con:
        df_leads.to_sql(
            name=table_name.lower(), 
            con=con, 
            if_exists=if_exists
        )

def test_select_datos():
    """
    Test the connection to the PostgreSQL database and retrieve data from the 'alumnos' and 'leads' tables.

    Environment Variables:
        DB_USER (str): Database username.
        DB_PASSWORD (str): Database password.
        DB_NAME (str): Database name.
        ACCOUNT_IDENTIFIER (str): Host identifier for the database.

    Database Operations:
        - Connects to the database using psycopg2.
        - Executes SELECT queries on 'alumnos' and 'leads' tables.
        - Prints the number of records retrieved from each table.

    Returns:
        tuple: A tuple containing two lists:
            - resultados_alumnos (list): Records retrieved from the 'alumnos' table.
            - resultados_leads (list): Records retrieved from the 'leads' table.

    Notes:
        Handles common connection errors such as invalid password or connection issues.
    """
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    ACCOUNT_IDENTIFIER = os.getenv("ACCOUNT_IDENTIFIER")

    try:
        # Connect to the database
        connection = psycopg2.connect(
            database=DB_NAME, 
            user=DB_USER, 
            password=DB_PASSWORD, 
            host=ACCOUNT_IDENTIFIER
        )
        print("Conexión realizada con éxito")

    except OperationalError as e:
        # Handle common connection errors
        if e.pgcode == errorcodes.INVALID_PASSWORD:
            print("Contraseña inválida.")
        elif e.pgcode == errorcodes.CONNECTION_EXCEPTION:
            print("Error de conexión.")
        else:
            print(f"Ocurrió un error: {e}")
        return [], []

    # Create a cursor to execute queries
    cursor = connection.cursor()

    # Execute SELECT query on 'alumnos'
    cursor.execute('SELECT * FROM "alumnos";')
    resultados_alumnos = cursor.fetchall()
    print(f"Resultados en la tabla alumnos: {len(resultados_alumnos)}")

    # Execute SELECT query on 'leads'
    cursor.execute('SELECT * FROM "leads";')
    resultados_leads = cursor.fetchall()
    print(f"Resultados en la tabla leads: {len(resultados_leads)}")

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return resultados_alumnos, resultados_leads
