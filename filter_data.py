import pandas as pd
from utils.data_cleaning import clean_taxi_data
from progressbar import ProgressBar
import json
import time


with open('to_keep.json', 'r') as infile:
    to_keep = set(json.load(infile))


for month_num in range(1, 13):
    print month_num
    start_time = time.time()
    month_zfilled = unicode(month_num).zfill(2)
    df = pd.read_csv('data/yellow_tripdata_2015-{}.csv'.format(month_zfilled))

    # create route column
    for dt_col in ('tpep_pickup_datetime', 'tpep_dropoff_datetime'):
        df[dt_col] = df[dt_col].astype('datetime64')

    df['pickup_lat_coord'] = np.floor((df['pickup_latitude'] - min_lat) / lat_chunk_size).astype(np.int)
    df['pickup_lng_coord'] = np.floor((df['pickup_longitude'] - min_lng) / lng_chunk_size).astype(np.int)
    df['dropoff_lat_coord'] = np.floor((df['dropoff_latitude'] - min_lat) / lat_chunk_size).astype(np.int)
    df['dropoff_lng_coord'] = np.floor((df['dropoff_longitude'] - min_lng) / lng_chunk_size).astype(np.int)
    df['pickup_coords'] = df['pickup_lat_coord'].astype(str).str.cat(df['pickup_lng_coord'].astype(str), sep=', ')
    df['dropoff_coords'] = df['dropoff_lat_coord'].astype(str).str.cat(df['dropoff_lng_coord'].astype(str), sep=', ')
    df['route'] = df['pickup_coords'].str.cat(df['dropoff_coords'], sep=' -> ')


    filtered = df[df['route'].isin(to_keep)]
    
    # exclude points with 0 lat or lng
    filtered = filtered[(filtered['pickup_latitude'] != 0) & (filtered['pickup_longitude'] != 0) & (filtered['dropoff_latitude'] != 0) & (filtered['dropoff_latitude'] != 0)]    

    filtered['is_weekday'] = filtered['tpep_pickup_datetime'].apply(lambda x: 0 if x.weekday > 4 else 1)
    filtered['pickup_day_hour'] = filtered.is_weekday.astype(str).str.cat(filtered.tpep_pickup_datetime.dt.hour.astype(str), sep=', ')
    filtered['trip_duration'] = (filtered['tpep_dropoff_datetime'] - filtered['tpep_pickup_datetime'])
    filtered['group_id'] = filtered['route'].str.cat(filtered['pickup_day_hour'], sep=' at ')
    filtered.to_csv('filtered_data/2015-{}'.format(month_zfilled))

    print "Took {}s".format(time.time() - start_time)
    print "\n\n"
