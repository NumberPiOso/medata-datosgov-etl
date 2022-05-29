# Integration open data

This is the final project of the udacity's
[Data Engineering Nanodegree Program](https://www.udacity.com/course/data-engineer-nanodegree--nd027?utm_source=gsem_brand&utm_medium=ads_r&utm_campaign=12908423264_c_individuals&utm_term=123085792713&utm_keyword=nanodegree%20data%20engineer_e&gclid=CjwKCAjws8yUBhA1EiwAi_tpERI2Q4lWT-GS2_nJVLj272T1eeszn_Ow11sOMNzrOseyS89JrYxLHhoCnlEQAvD_BwE).  
  
In this project, information of homicides and thefts in the city of Medellin
are integrated with the information of the postal codes.  

The code separates in an ETL process which extracts data from 
[medata](http://medata.gov.co/) and
[datos.gov](https://www.datos.gov.co/Ordenamiento-Territorial/)
and load them into a Postgres Database.  
  
By using Kimball's data modeling technique [[1]](#1) dimensions and fact tables
are createda and saved into the star schema.

## Code structure
📦data
📦etl (Extraction, transformation and loading processes)
📦science (Some demonstrations of what can be done with the data)
📜.env (database environment variables)
📜README.md (This file)
📜environment.yml (Python environment)

## Developing

For developing, we have the following requirements.
- [Anaconda](https://www.anaconda.com/) for Python environment.
- [A Postgres database](https://www.postgresql.org/) (It can be a local or cloud database or a data warehouse as Amazon Redshift).  
  
Define the database environment variables described in `.env.example`.
For this, you could save this file as `.env` with the correct credentials and
run `export $(cat ../.env | xargs)` or define manually this variables.  
  
To create and use the anaconda environment
```bash
conda env create -f environment.yml
conda activate medata_integration
```

## Considerations

### Database

Since the 


## Data
All data referenced in this project is from Medellín, Colombia.

[Thefts recorded by the National Police committed against people in public spaces. (Medata)](http://medata.gov.co/dataset/hurto-persona)
[Homicides registered by the review and validation table for homicide cases. (Medata)](http://medata.gov.co/dataset/homicidio)
[TMap of Postal Codes - Municipality of Medellín (datos.gov)](https://www.datos.gov.co/Ordenamiento-Territorial/Mapa-de-C-digos-Postales-Municipio-de-Medell-n/9z4i-tgzy)


## References

<a id="1">[1]</a>M. Ross and R. Kimball, The data warehouse toolkit. Hoboken, N.J.: Wiley, 2013.
