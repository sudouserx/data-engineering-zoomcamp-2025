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
#         --host pg-database \
#         --port 5432 \
#         --db ny_taxi \
#         --table_name green_taxi_trips \
#         --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"'