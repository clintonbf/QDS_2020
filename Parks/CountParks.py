import pandas as pd

data = pd.read_csv (r'/Users/anguslin/Downloads/QDS_Hacks/RegionScore/RegionScore/Parks/parks.csv', sep=';', engine='python')
df = pd.DataFrame(data, columns= ['ParkID', 'NeighbourhoodName'])
df2 = df.groupby('NeighbourhoodName').count()
print (df2)

Export = df2.to_json(r'/Users/anguslin/Downloads/QDS_Hacks/RegionScore/RegionScore/Parks/countedParks.json')


