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

    os.system(f"wget {url} -O {data}")
    os.system(f"gunzip -c {data} > {csv_name}")

    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')
    conn = engine.connect()

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    # Process first chunk
    df = next(df_iter)
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    # Create table with correct schema
    df.head(n=0).to_sql(name=table_name, con=conn, if_exists='replace')
    # Insert first chunk
    df.to_sql(name=table_name, con=conn, if_exists='append')

    # Process remaining chunks
    while True:
        try:
            df = next(df_iter)
            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
            df.to_sql(name=table_name, con=conn, if_exists='append')
        except StopIteration:
            print("Data ingestion completed.")
            break

    conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    parser.add_argument('--user', required=True)
    parser.add_argument('--password', required=True)
    parser.add_argument('--host', required=True)
    parser.add_argument('--port', required=True)
    parser.add_argument('--db', required=True)
    parser.add_argument('--table_name', required=True)
    parser.add_argument('--url', required=True)

    args = parser.parse_args()
    main(args)