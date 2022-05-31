import sys
from pathlib import Path

from sqlalchemy import text

if __name__ == "__main__":
    sys.path.insert(0, str(Path.cwd().resolve()))  # Add database path
    from database import engine

    # Create dimensions
    tbls_dims_not_nulls = [
        ("star.dim_comuna", "COMUNA_KEY"),
        ("star.dim_age", "age_key"),
        ("star.dim_gender", "gender_key"),
    ]
    queryf = (
        lambda tbl, col: f'SELECT COUNT(*) FROM {tbl} WHERE "{col}" IS NULL'
    )
    expected = 0
    for tbl, col in tbls_dims_not_nulls:
        print(queryf(tbl, col))
        sql = text(queryf(tbl, col))
        records = engine.execute(sql)
        num_records = records.first()[0]
        if num_records != 0:
            raise ValueError(
                f"Data quality check failed. {tbl} contained {num_records}"
                f"rows with {col} nulls"
            )
