import snowflake.connector
import pandas as pd
import numpy as np
from dateutil.parser import parse

# Connect to the Snowflake database
conn = snowflake.connector.connect(
    user='bruno.campos@saltpay.co',
    authenticator='externalbrowser',
    account='zrgzuap-fa15311',
    warehouse='DATA_ANALYSTS',
    role='BRUNOC',
    database='BRUNOC',
    schema='SALTPAY'
)

# Define the SQL query to get data from a table
query = "SELECT TRY_TO_TIMESTAMP(created_at, 'mm/dd/yyyy HH:MI:SS AM TZH:TZM') AS custom_date_cast"
query += ", TRY_TO_TIMESTAMP(created_at) AS default_date_cast"
query += ", CREATED_AT "
query += "FROM BRUNOC.SALTPAY.TEST_BASKET_DATA " 
query += "WHERE TRY_TO_TIMESTAMP(created_at, 'mm/dd/yyyy HH:MI:SS AM TZH:TZM') IS NULL AND TRY_TO_TIMESTAMP(created_at) IS NULL"

# Load query to a df
df = pd.read_sql(query, conn)

df['CREATED_AT_PARSED'] = df['CREATED_AT'].apply(lambda x: parse(x))

print(df.head())

# Save the first 5 rows of the DataFrame to a CSV file
df.head().to_csv('output.csv', index=False)

conn.close()
