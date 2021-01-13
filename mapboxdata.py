import pandas
import geopandas as gpd
import shapely.wkt
import shapely.geometry
import numpy as np

#Read trip data
df = pandas.read_csv('datasets/trips_4_mapbox_algo.csv')


df['date mapped'] = pandas.to_datetime(df['date mapped'])

df.set_index('date mapped', inplace=True)

#get only trips with more than 1 stop
df2 = df[df['number of stops']>1]

#rename column
df2 = df2.rename(columns={'geometry (wkt)':'geometry'})

#prepare for conversion to geodataframe
geometry = df2['geometry'].map(shapely.wkt.loads)
df2 = df2.drop('geometry', axis=1)

#convert to geodataframe
gdf = gpd.GeoDataFrame(df2, crs="EPSG:4326", geometry=geometry)


#prepare plotting on MapBox

lats = []
lons = []
names = []
dates = []
assoc = []
routes = []
vehicles =[]
trips=[]
cities=[]
modes = []

for feature, name, date,company,route,vehicle,trip,city,mode in zip(gdf.geometry, gdf.mapper,gdf.index,gdf['company'],gdf['route_id'],gdf['vehicle reg no'],gdf['trip id'],gdf['city'],gdf['vehicle type']):
    if isinstance(feature, shapely.geometry.linestring.LineString):
        linestrings = [feature]
    elif isinstance(feature, shapely.geometry.multilinestring.MultiLineString):
        linestrings = feature.geoms
    else:
        continue
    for linestring in linestrings:
        x, y = linestring.xy
        
        lats = np.append(lats, y)
        lons = np.append(lons, x)
        
        names = np.append(names, [name]*len(y))
        assoc = np.append(assoc, [company]*len(y))
        routes = np.append(routes, [route]*len(y))
        vehicles = np.append(vehicles, [vehicle]*len(y))
        dates = np.append(dates, [date]*len(y))
        trips = np.append(trips, [trip]*len(y))
        cities = np.append(cities, [city]*len(y))
        modes = np.append(modes, [mode]*len(y))



        lats = np.append(lats, None)
        lons = np.append(lons, None)
        names = np.append(names, None)
        assoc = np.append(assoc, None)
        routes = np.append(routes, None)
        vehicles = np.append(vehicles, None)
        dates = np.append(dates, None)
        trips = np.append(trips, None)
        cities = np.append(cities, None)
        modes = np.append(modes, None)


lat = lats.tolist()
lon = lons.tolist()
date = dates.tolist()
assoc = assoc.tolist()
vehicle = vehicles.tolist()
route = routes.tolist()
name = names.tolist()
trip = trips.tolist()
city = cities.tolist()
mode = modes.tolist()


df = pandas.DataFrame(list(zip(lat, lon,date,assoc,vehicle,route,name,trip,city,mode)),columns =['lat', 'lon','date','company','vehicleReg','routeName','mapperName','trip id','city','vehicle type'])
df = df.set_index('date')
df = df.dropna()
df = df.drop_duplicates()

df.to_csv(r'datasets/mapbox_trips_output.csv')
#print(df.head())