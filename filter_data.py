import pandas as pd
from utils.data_cleaning import clean_taxi_data
from progressbar import ProgressBar
import json


with open('to_keep.json', 'r') as infile:
    to_keep = set(json.load(infile))

pbar = ProgressBar()

for month_num in pbar(range(1, 13)):
    month_zfilled = unicode(month_num).zfill(2)
    df = pd.read_csv('data/yellow_tripdata_2015-{}.csv'.format(month_zfilled))
    df = clean_taxi_data(df)
    filtered = df[df['route'].isin(to_keep)]
    filtered['group_id'] = filtered['route'].str.cat(filtered['pickup_day_hour'], sep=' at ')
    filtered.to_csv('filtered_data/2015-{}'.format(month_zfilled))

