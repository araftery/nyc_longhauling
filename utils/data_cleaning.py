import numpy as np
from grid import *


def clean_taxi_data(df):
    for dt_col in ('tpep_pickup_datetime', 'tpep_dropoff_datetime'):
        df[dt_col] = df[dt_col].astype('datetime64')
    df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime'])

    # exclude points with 0 lat or lng
    df = df[(df['pickup_latitude'] != 0) & (df['pickup_longitude'] != 0) & (df['dropoff_latitude'] != 0) & (df['dropoff_latitude'] != 0)]

    df['pickup_lat_coord'] = np.floor((df['pickup_latitude'] - min_lat) / lat_chunk_size).astype(np.int)
    df['pickup_lng_coord'] = np.floor((df['pickup_longitude'] - min_lng) / lng_chunk_size).astype(np.int)
    df['dropoff_lat_coord'] = np.floor((df['dropoff_latitude'] - min_lat) / lat_chunk_size).astype(np.int)
    df['dropoff_lng_coord'] = np.floor((df['dropoff_longitude'] - min_lng) / lng_chunk_size).astype(np.int)
    df['pickup_coords'] = df['pickup_lat_coord'].astype(str).str.cat(df['pickup_lng_coord'].astype(str), sep=', ')
    df['dropoff_coords'] = df['dropoff_lat_coord'].astype(str).str.cat(df['dropoff_lng_coord'].astype(str), sep=', ')
    df['route'] = df['pickup_coords'].str.cat(df['dropoff_coords'], sep=' -> ')
    df['pickup_day_hour'] = df.tpep_pickup_datetime.dt.day.astype(str).str.cat(df.tpep_pickup_datetime.dt.hour.astype(str), sep=', ')

    return df
