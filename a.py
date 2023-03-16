import pandas as pd
date_from = '2019-01-01'
date_to = '2019-01-12'
date_range = pd.date_range(date_from, date_to, freq='D')
print(date_range)