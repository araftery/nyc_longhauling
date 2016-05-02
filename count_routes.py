import pandas as pd
from utils.data_cleaning import clean_taxi_data
from progressbar import ProgressBar

pbar = ProgressBar()

for month_num in pbar(range(1, 13)):
    month_zfilled = unicode(month_num).zfill(2)
    df = pd.read_csv('cleaned_data/2015-{}.csv'.format(month_zfilled))
    df = clean_taxi_data(df)
    df['route'].value_counts().to_csv('counts/2015-{}'.format(month_zfilled))
