import pandas as pd
from sqlalchemy import create_engine
import argparse
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'
    data = 'data.csv.gz'

    # Download the file
    os.system(f"wget {url} -O {data}")

    # Extract the gzipped CSV
    os.system(f"gunzip -c {data} > {csv_name}")

    # Create and connect with PostgreSQL
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Use iterator to divide it into chunks
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    # Insert the table schema
    df = next(df_iter)
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    # Insert all chunks iteratively
    while True:
        try:
            df = next(df_iter)
            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
            df.to_sql(name=table_name, con=engine, if_exists='append')
        except StopIteration:
            print("Data ingestion complete.")
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='IngestData',
        description='Ingest CSV data into PostgreSQL container',
        epilog='You need user, password, host, port, database name, table_name, and the URL of the CSV.'
    )

    parser.add_argument('--user', required=True, help='User name for PostgreSQL')
    parser.add_argument('--password', required=True, help='Password for PostgreSQL')
    parser.add_argument('--host', required=True, help='Host for PostgreSQL')
    parser.add_argument('--port', required=True, help='Port for PostgreSQL')
    parser.add_argument('--db', required=True, help='Database name for PostgreSQL')
    parser.add_argument('--table_name', required=True, help='Table name to write the results to')
    parser.add_argument('--url', required=True, help='URL of the CSV file')

    args = parser.parse_args()

    # Execute the main function
    main(args)
