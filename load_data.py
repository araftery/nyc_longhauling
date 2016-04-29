import setup
import time

import pandas as pd

from db.models import Trip
from utils.data_cleaning import clean_taxi_data


df = pd.read_csv('data/yellow_tripdata_2015-12.csv')
df = clean_taxi_data(df)

total_rows = df.shape[0]

start_time = time.time()
for i, row in df.iterrows():
    Trip.objects.create(
        pickup_time=row['tpep_pickup_datetime'],
        dropoff_time=row['tpep_dropoff_datetime'],
        passenger_count=row['passenger_count'],
        distance=row['trip_distance'],
        pickup_longitude=row['pickup_longitude'],
        pickup_latitude=row['pickup_latitude'],
        dropoff_longitude=row['dropoff_longitude'],
        dropoff_latitude=row['dropoff_latitude'],
        fare_amount=row['fare_amount'],
        extra=row['extra'],
        mta_tax=row['mta_tax'],
        tip_amount=row['tip_amount'],
        tolls_amount=row['tolls_amount'],
        pickup_lat_coord=row['pickup_lat_coord'],
        pickup_lng_coord=row['pickup_lng_coord'],
        dropoff_lat_coord=row['dropoff_lat_coord'],
        dropoff_lng_coord=row['dropoff_lng_coord'],
        pickup_day_hour=row['pickup_day_hour'],
    )

    if i % 50000 == 0:
        print "{} rows, {:2.2f}% done. Time elapsed: {} secs".format(i, (float(i) / total_rows) * 100, time.time() - start_time)
