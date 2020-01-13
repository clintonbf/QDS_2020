import pandas as pd

data = pd.read_csv (r'/Users/anguslin/Downloads/QDS_Hacks/RegionScore/RegionScore/RapidTransit/rapid-transit-stations.csv', sep=';', engine='python')
df = pd.DataFrame(data, columns= ['STATION', 'Geo Local Area'])
df2 = df.groupby('Geo Local Area').count()
print (df2)

Export = df2.to_json(r'/Users/anguslin/Downloads/QDS_Hacks/RegionScore/RegionScore/RapidTransit/countedRapidTransit.json')

'''
Ideas For Calculating Score:
1. School
2. Transit
3. Parks
4. Rental Standard

ie pick School -> Rental Standard -> Transit -> Parks
50% -> 30% -> 15% -> 5%

If we are going by Compatibility Score: then use
 - highest region number / current region number
 - highest region number will have get full score for the ranking 50% or 30% etc
 - others will get maybe 25% out of 50% if has half as much as highest.

'''

'''
Front End?


'''
