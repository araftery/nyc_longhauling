import setup

import pandas as pd

from utils.data_cleaning import clean_taxi_data


cols = ['tpep_pickup_datetime',
    'tpep_dropoff_datetime',
    'passenger_count',
    'trip_distance',
    'pickup_longitude',
    'pickup_latitude',
    'dropoff_longitude',
    'dropoff_latitude',
    'fare_amount',
    'extra',
    'mta_tax',
    'tip_amount',
    'tolls_amount',
    'pickup_lat_coord',
    'pickup_lng_coord',
    'dropoff_lat_coord',
    'dropoff_lng_coord',
    'pickup_day_hour']

for i in [11]:
    df = pd.read_csv('data/yellow_tripdata_2015-{:02d}.csv'.format(i))
    df = clean_taxi_data(df)
    df[cols].to_csv('cleaned_data/2015-{:02d}.csv'.format(i), index=False)
