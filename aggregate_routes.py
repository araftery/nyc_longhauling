import pandas as pd
from progressbar import ProgressBar

pbar = ProgressBar()

dfs = []
for month_num in pbar(range(1, 13)):
    month_zfilled = unicode(month_num).zfill(2)
    df = pd.read_csv('./counts/2015-{}'.format(month_zfilled), names=['route', 'count'], header=None)
    dfs.append(df)

pd.concat(dfs).groupby('route', as_index=False)['count'].sum().sort_values('count', ascending=False).to_csv('counts/aggregated.csv')
