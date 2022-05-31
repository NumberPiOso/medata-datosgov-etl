import itertools
import sys
from pathlib import Path

from sqlalchemy import text

if __name__ == "__main__":
    sys.path.insert(0, str(Path.cwd().resolve()))  # Add database path
    from database import engine

    # Fact tables
    fact_tbls = ["star.fact_kill", "star.fact_steal"]

    # Create dimensions
    tbls_dims_not_nulls = [
        ("star.dim_comuna", "COMUNA_KEY"),
        ("star.dim_age", "age_key"),
        ("star.dim_gender", "gender_key"),
    ]

    for fact_tbl, (dim_tbl, col) in itertools.product(
        fact_tbls, tbls_dims_not_nulls
    ):
        sql = text(f"SELECT COUNT(*) FROM {fact_tbl} a")
        records = engine.execute(sql)
        num_records_original = records.first()[0]

        sql_join = text(
            f"SELECT COUNT(*) FROM {fact_tbl} a JOIN {dim_tbl} b ON a.{col} = b.{col}"
        )
        records = engine.execute(sql)
        new_num_records = records.first()[0]
        if num_records_original != new_num_records:
            raise ValueError(
                f"Data quality check failed. Joining {fact_tbl} with {dim_tbl}"
                f"Originally {fact_tbl} has {num_records_original} rows."
                f"But after the join with {dim_tbl} it results with"
                f"{new_num_records} rows"
            )
