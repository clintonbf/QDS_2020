import pandas as pd

data = pd.read_csv (r'/Users/anguslin/Downloads/QDS_Hacks/RegionScore/RegionScore/Schools/schools.csv', sep=';', engine='python')
df = pd.DataFrame(data, columns= ['SCHOOL_NAME', 'Geo Local Area'])
df2 = df.groupby('Geo Local Area').count()
print (df2)

Export = df2.to_json(r'/Users/anguslin/Downloads/QDS_Hacks/RegionScore/RegionScore/Schools/countedSchools.json')

