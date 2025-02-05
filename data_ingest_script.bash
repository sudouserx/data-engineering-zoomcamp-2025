## LOCAL DATA INGESTION

# URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"
# python ingest_data.py \
#     --user=root \
#     --password=root \
#     --host=localhost \
#     --port=5432 \
#     --db=ny_taxi \
#     --table_name=green_taxi_trips \
#     --url=${URL}


# # DOCKERIZING DATA PIPELINE

# bash -c 'docker build -t taxi_ingest:v001 .'

# bash -c 'docker run -it \
#     --network=pg-network \
#     taxi_ingest:v001 \
#         --user root \
#         --password root \
#         --host pgdatabase \
#         --port 5432 \
#         --db ny_taxi \
#         --table_name zones \
#         --url="https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"'


# ingest zone lookup table 
# python test.py \
#     --user root \
#     --password root \
#     --host localhost \
#     --port 5432 \
#     --db ny_taxi \
#     --table_name zones \
#     --url "/home/ebrahim/Desktop/docker_test/taxi_zone_lookup.csv"