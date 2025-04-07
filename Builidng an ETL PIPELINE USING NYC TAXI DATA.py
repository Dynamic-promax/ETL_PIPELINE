import pandas as pd
df=pd.read_csv(r"C:\\Users\\DELL\\Desktop\\Data Engineering NEW\\taxi_zone_lookup.csv")
print(df.head())
df.dropna(subset=["Borough", "Zone", "service_zone"], inplace=True)

print(df)


# LOAD: SAVE TRANSFORMED DATA INTO POSTGRESQL
#Database connection details
from sqlalchemy import create_engine
from urllib.parse import quote_plus
db_user = "postgres"
db_password = quote_plus("ALFA")
db_host = "localhost"
db_port = "5432"
db_name = "sales_dp"

# Create database connection
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

#Load data into postgreSQL
df.to_sql("TAXI DATA", engine, if_exists="replace", index=False)
print("Data successfully loaded into PostgreSQL")
