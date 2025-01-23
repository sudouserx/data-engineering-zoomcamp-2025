import pandas as pd
from sqlalchemy import create_engine
import argparse # python standard parser
import os

def main(params) :

    user = params.user
    password = user.password
    host = user.host
    port = user.port
    db = user.db
    table_name = user.table_name
    url = user.url
    csv_name = 'output.csv'

    os.system(f"wget {url} -O {csv_name}")

    # TODO : extract if it is in tar.gz format

    # create and connect with postgresql 
    engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{db}')
    # engine.connect() # ??

    # use iterator to divide it into chunks of size 100000 , since it is hard to run it at once 
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    # insert the head of the table_name, and if the name exists already .. replace it
    df.head(n=0).to_sql(name='{table_name}', con=engine, if_exists='replace')

    # insert all chunks iteratively
    while True :
        df = next(df_iter)
        
        df.lpep_pickup_datetime= pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime= pd.to_datetime(df.lpep_dropoff_datetime)
        df.to_sql(name='{table_name}', con=engine, if_exists='append')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                        prog='IngestData',
                        description='Ingest CSV data into postgres container',
                        epilog='You need user , password , host , port, database name , table_name , url of the csv')

    parser.add_argument('user', help='user name for postgres')
    parser.add_argument('passwrod', help='passwrod for postgres')
    parser.add_argument('host', help='host for postgres')
    parser.add_argument('port', help='port for postgres')
    parser.add_argument('db', help='database name for postgres')
    parser.add_argument('table_name', help='table_name name where we write the results to ')
    parser.add_argument('url', help='url of the csv file')

    args = parser.parse_args()

    # execute 
    main(args)



