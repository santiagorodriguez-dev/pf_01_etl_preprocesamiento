import pandas as pd
import sys
sys.path.append("../")
import dotenv # type: ignore
dotenv.load_dotenv()

from src import support_faker as fk
from src import support_bd as bd

def generate_data_set():
   print("Inicio creacion de dataset")
   df_alumnos = fk.load_data_init_alumnos()
   df_leads = fk.load_data_init_leads()
   df_leads, df_alumnos = fk.remove_duplicates(df_leads, df_alumnos)
   print("Numero de df_leads: ", df_leads.shape[0])
   print("Numero de df_alumnos: ", df_alumnos.shape[0])
   bd.create_table_insert(df_alumnos, df_leads)
   bd.test_select_datos()

def main():
   generate_data_set()
   
if __name__ == "__main__":
   main()
