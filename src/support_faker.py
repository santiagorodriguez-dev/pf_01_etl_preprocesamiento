# Importaciones
import pandas as pd # type: ignore
import sys
sys.path.append("../")
from faker import Faker # type: ignore
from faker.providers import DynamicProvider # type: ignore

import dotenv # type: ignore
import numpy as np # type: ignore
dotenv.load_dotenv()
from openai import OpenAI # type: ignore
import string
import random
from datetime import datetime



def load_data_init_alumnos(num_registros: int = 10001):
    """
    Genera un DataFrame simulado con datos de alumnos utilizando la biblioteca Faker.

    Args:
        num_registros (int): Número de registros a generar. Por defecto es 10001.

    Returns:
        pd.DataFrame: DataFrame con columnas como nombre, apellidos, email, estudios, especialidad, ciudad, edad, 
        teléfono, sexo y motivo de compra.

    Notas:
        - Utiliza Faker para simular datos realistas.
        - Los datos generados incluyen detalles como estudios, especialidades y motivos de compra personalizables.
        - Se eliminan los registros duplicados basados en la columna 'email'.
    """

    
    type_estudios = DynamicProvider(
     provider_name="estudios",
     elements=["Eso", "Bachillerato", "Grado Medio", "Grado Superior", "Licenciatura", "Grado", "Máster", "Doctorado"],
    )

    type_estudios_especialidad = DynamicProvider(
     provider_name="especialidad",
     elements=["Informatica", "Ingenieria", "Letras"],
    )

    type_motivo_compra_alumnos = DynamicProvider(
     provider_name="motivo_compra_alumnos",
     elements=["estoy en el paro", "tener teletrabajo", "mejorar empleablidad","Cambio de sector", "Mejorar mi formación", "Tener mas poder adquisitivo"],
    )
    
    fake = Faker('es_ES')
    Faker.seed(4321)
    fake.add_provider(type_estudios)
    fake.add_provider(type_estudios_especialidad)
    fake.add_provider(type_motivo_compra_alumnos)


    data = [
             { "nombre": fake.first_name(),
               "apellidos":  fake.last_name(),
               "email": fake.email(),
               "estudios": fake.estudios(),
               "especialidad": fake.especialidad(),
               "ciudad": fake.address().split('\n')[1].split(',')[0],
               "edad": np.random.randint(18, 45),
               "telefono": fake.phone_number(),
               "sexo": random.choices(['Hombre', 'Mujer'], weights=[0.5, 0.5], k=1)[0],
               "motivo_compra":fake.motivo_compra_alumnos()
             }
             for i in range(num_registros)
         ]
    
    df = pd.DataFrame(data = data).drop_duplicates(subset=['email'], keep='first', inplace=False)

    return df


def load_data_init_leads(num_registros: int = 1001):
    """
    Genera un DataFrame simulado con datos de leads utilizando la biblioteca Faker.

    Args:
        num_registros (int): Número de registros a generar. Por defecto es 1001.

    Returns:
        pd.DataFrame: DataFrame con columnas como nombre, apellidos, email, estudios, especialidad, ciudad, edad, 
        teléfono, sexo y motivo de compra.

    Notas:
        - Utiliza Faker para simular datos realistas.
        - Los datos generados incluyen motivos de compra específicos para leads, además de otros datos básicos.
        - Se eliminan los registros duplicados basados en la columna 'email'.
    """

    
    type_estudios = DynamicProvider(
     provider_name="estudios",
     elements=["Eso", "Bachillerato", "Grado Medio", "Grado Superior", "Licenciatura", "Grado", "Máster", "Doctorado"],
    )

    type_estudios_especialidad = DynamicProvider(
     provider_name="especialidad",
     elements=["Informatica", "Ingenieria", "Letras"],
    )

    type_motivo_compra_leads = DynamicProvider(
     provider_name="motivo_compra_leads",
     elements = [
      "Demanda laboral en constante crecimiento",
      "Versatilidad en el mercado tecnológico",
      "Incremento en las oportunidades salariales",
      "Desarrollo de habilidades multidisciplinarias",
      "Capacidad para liderar proyectos tecnológicos",
      "Competitividad profesional a largo plazo",
      "Comprensión integral del ciclo de desarrollo de software",
      "Acceso a roles técnicos y estratégicos",
      "Mejora en la comunicación entre equipos front-end y back-end",
      "Alta demanda en startups y empresas consolidadas",
      "Capacidad de adaptación a diferentes industrias",
      "Potencial para trabajar en proyectos internacionales",
      "Fortalecimiento del perfil profesional frente a reclutadores",
      "Contribución al avance tecnológico de las empresas",
      "Preparación para transicionar hacia roles de CTO o Tech Lead",
      "Querer resolver problemas sin depender de otros",
      "Ganas de crear proyectos propios de inicio a fin",
      "Sentirse 'el maestro Jedi' del desarrollo web",
      "Curiosidad por aprender de todo un poco",
      "Mayor libertad al buscar empleo remoto",
      "Ahorrar dinero en equipos de desarrollo para proyectos personales",
      "Impresionar a amigos o colegas con soluciones completas",
      "Hacer realidad ideas locas con código",
      "Disfrutar aprendiendo nuevas tecnologías constantemente",
      "Por amor a los desafíos y romper barreras técnicas",
      "Tener más control sobre proyectos creativos",
      "Explorar la satisfacción de construir algo desde cero",
      "Ser un 'todoterreno' en cualquier proyecto tecnológico",
      "Desarrollar videojuegos o apps personales",
      "Combinar hobbies con programación para proyectos únicos",
      "Aventurarse en el mundo freelance con más confianza",
      "Evitar la frustración de esperar a que otro termine una tarea",
      "Orgullo personal por dominar ambos lados del desarrollo",
      "Ampliar las posibilidades de networking con otros desarrolladores"
]) 
   
    fake = Faker('es_ES')
    Faker.seed(8960)
    fake.add_provider(type_estudios)
    fake.add_provider(type_estudios_especialidad)
    fake.add_provider(type_motivo_compra_leads)

    data = [
             { "nombre": fake.first_name(),
               "apellidos":  fake.last_name(),
               "email": fake.email(),
               "estudios": fake.estudios(),
               "especialidad": fake.especialidad(),
               "ciudad": fake.address().split('\n')[1].split(',')[0],
               "edad": np.random.randint(18, 45),
               "telefono": fake.phone_number(),
               "sexo": random.choices(['Hombre', 'Mujer'], weights=[0.5, 0.5], k=1)[0],
               "motivo_compra":fake.motivo_compra_leads()
             }
             for i in range(num_registros)
         ]
    
    df = pd.DataFrame(data = data).drop_duplicates(subset=['email'], keep='first', inplace=False)

    return df

def remove_duplicates(df_leads, df_alumnos):
    """
    Elimina duplicados entre los DataFrames de leads y alumnos basándose en la columna 'email'.

    Args:
        df_leads (pd.DataFrame): DataFrame con los datos de leads.
        df_alumnos (pd.DataFrame): DataFrame con los datos de alumnos.

    Returns:
        tuple: Una tupla con los DataFrames actualizados (df_leads, df_alumnos) sin registros duplicados en base a 'email'.

    Notas:
        - Realiza un merge interno para identificar duplicados.
        - Elimina los emails duplicados de ambos DataFrames.
        - Reemplaza saltos de línea en el contenido de los DataFrames.
        - Reinicia los índices de ambos DataFrames después de limpiar duplicados.
    """

    
    result = pd.merge(df_leads, df_alumnos, on=['email'], how='inner')

    for i in result['email']:
      df_leads = df_leads.loc[df_leads['email'] != i]
    
    for i in result['email']:
      df_alumnos = df_alumnos.loc[df_alumnos['email'] != i]

      df_leads = df_leads.replace(r'\n',  ' ', regex=True)
      df_alumnos = df_alumnos.replace(r'\n',  ' ', regex=True)

      df_leads.reset_index(drop=True, inplace=True)
      df_alumnos.reset_index(drop=True, inplace=True)

    return (df_leads, df_alumnos)

def save_df_to_csv(df_leads, df_alumnos):
  """
    Guarda los DataFrames de leads y alumnos en archivos CSV.

    Args:
        df_leads (pd.DataFrame): DataFrame con los datos de leads.
        df_alumnos (pd.DataFrame): DataFrame con los datos de alumnos.

    Returns:
        None

    Notas:
        - Los DataFrames se guardan en la carpeta "../data/" con los nombres 'leads.csv' y 'alumnos.csv'.
        - Incluye encabezados y mantiene los índices en los archivos generados.
        - Imprime el número de registros en cada DataFrame antes de guardar.
    """


  print("Numero de df_leads: ", df_leads.shape[0])
  print("Numero de df_alumnos: ", df_alumnos.shape[0])

  df_leads.to_csv(f"../data/leads.csv", index=True, header=True)
  df_alumnos.to_csv(f"../data/alumnos.csv", index=True, header=True)




