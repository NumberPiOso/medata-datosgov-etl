import os
import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd

if __name__ == "__main__":
    sys.path.insert(0, str(Path.cwd().resolve()))  # Add database path
    from database import engine

    schema = "stg"
    save_data_path = os.getenv("STG_DATA_PATH")
    cols_to_extract = [
        "fecha_hecho",
        "cantidad",
        "latitud",
        "longitud",
        "sexo",
        "edad",
        "estado_civil",
        "nombre_barrio",
        "codigo_barrio",
        "codigo_comuna",
    ]

    # load homicidio
    homicidio = pd.read_csv("../data/homicidio.csv", sep=";")
    homicidio = homicidio[cols_to_extract]
    with engine.begin() as con:
        homicidio.to_sql(
            "stg_homicidio", con=con, if_exists="replace", schema=schema
        )

    # load hurto
    hurto = pd.read_csv("../data/hurto_a_persona.csv", sep=";")
    hurto = hurto[cols_to_extract]
    with engine.begin() as con:
        hurto.to_sql("stg_hurto", con=con, if_exists="replace", schema=schema)

    # load comunas
    map_comunas = gpd.read_file("../data/comunas.geojson")
    map_comunas.to_postgis(
        "stg_comunas", con=engine, if_exists="replace", schema=schema
    )
