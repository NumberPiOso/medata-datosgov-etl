query_dim_comuna = """
    DROP TABLE IF EXISTS star.dim_comuna;
    SELECT
        CAST("CODIGO" AS INT) AS "COMUNA_KEY"
        , "CODIGO"
        , "NOMBRE"
        , "IDENTIFICACION"
        , CAST("SUBTIPO_COMUNACORREGIMIENTO" AS SMALLINT) "SUBTIPO_COMUNACORREGIMIENTO"
        , "SHAPE.AREA", "SHAPE.LEN", geometry
    INTO star.dim_comuna
    FROM stg.stg_comunas
    WHERE "CODIGO" ~ '^[0-9]*$' -- IS_INTEGER
    """

query_dim_edad = """
    drop table if exists star.dim_age;

    with ages as (
        select generate_series as age from generate_series(1,100)
    )
    select age as age_key,
        case
            when age < 18 then 'adolescente'
            when age < 60 then 'edad productiva'
            when age < 101 then 'tercera edad'
            else NULL
        end as age_group
    into star.dim_age
    from ages
    """

query_dim_genero = """
    DROP TABLE IF EXISTS star.dim_gender;
    with distinct_sexo as (
        select distinct sexo
        from stg.stg_hurto
    )
    select md5(sexo) as gender_key, sexo
    into star.dim_gender
    from distinct_sexo
"""

query_fact_steal = """
    DROP TABLE IF EXISTS star.fact_steal;

    SELECT
        "fecha_hecho" as "date"
        , "cantidad" as "qty"
        , "latitud" as "latitude"
        , "longitud" as "longitude"
        , md5("sexo") AS gender_key
        , "edad" as age_key
        , CAST(codigo_comuna as int) AS "COMUNA_KEY"
    INTO star.fact_steal
    FROM stg.stg_hurto
    WHERE "codigo_comuna" ~ '^[0-9]*$' -- IS_INTEGER
"""

query_fact_kill = """
    DROP TABLE IF EXISTS star.fact_kill;

    SELECT
        "fecha_hecho" as "date"
        , "cantidad" as "qty"
        , "latitud" as "latitude"
        , "longitud" as "longitude"
        , md5("sexo") AS gender_key
        , "edad" as age_key
        , CAST(codigo_comuna as int) AS "COMUNA_KEY"
    INTO star.fact_kill
    FROM stg.stg_homicidio
"""

queries_create_dims = [
    query_dim_comuna,
    query_dim_edad,
    query_dim_genero,
]

queries_create_facts = [query_fact_kill, query_fact_steal]
