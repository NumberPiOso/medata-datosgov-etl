import os
import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd
import queries
from sqlalchemy import text

if __name__ == "__main__":
    sys.path.insert(0, str(Path.cwd().resolve()))  # Add database path
    from database import engine

    # Create dimensions
    for query in queries.queries_create_dims:
        sql = text(query)
        result = engine.execute(sql)

    # Create fact tables
    for query in queries.queries_create_facts:
        sql = text(query)
        result = engine.execute(sql)
