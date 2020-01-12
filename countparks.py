import pandas as pd

import csv
import json

df = pd.read_csv ('parks.csv', sep=';', engine='python')
df2 = pd.DataFrame(df, columns= ['ParkID','NeighbourhoodName'])
# df2.set_index("ParkID")
print(df2)
df3 = df2.groupby('NeighbourhoodName').agg('count')
# df3.to_json('parks_aggr.json')
print(df3)