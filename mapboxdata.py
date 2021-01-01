# import pandas
# import geopandas as gpd
# import shapely.wkt
# import shapely.geometry
# import numpy as np

# #Read trip data
# df = pandas.read_csv('datasets/15547_Trips_20201230.csv')

# df['Date Mapped'] = pandas.to_datetime(df['Date Mapped'])

# df.set_index('Date Mapped', inplace=True)

# #get only trips with more than 1 stop
# df2 = df[df['Number Of Stops']>1]

# #rename column
# df = df2.rename(columns={'Geometry (WKT)':'geometry'})

# #prepare for conversion to geodataframe
# geometry = df['geometry'].map(shapely.wkt.loads)
# df = df.drop('geometry', axis=1)

# #convert to geodataframe
# gdf = gpd.GeoDataFrame(df, crs="EPSG:4326", geometry=geometry)


# #prepare plotting on MapBox

# lats = []
# lons = []
# names = []
# dates = []
# assoc = []
# routes = []
# vehicles =[]
# trips=[]

# for feature, name, date,company,route,vehicle,trip in zip(gdf.geometry, gdf.Mapper,gdf.index,gdf['Company'],gdf['Route Description'],gdf['1"Vehicle Reg No"'],gdf['Trip ID']):
#     if isinstance(feature, shapely.geometry.linestring.LineString):
#         linestrings = [feature]
#     elif isinstance(feature, shapely.geometry.multilinestring.MultiLineString):
#         linestrings = feature.geoms
#     else:
#         continue
#     for linestring in linestrings:
#         x, y = linestring.xy
        
#         lats = np.append(lats, y)
#         lons = np.append(lons, x)
        
#         names = np.append(names, [name]*len(y))
#         assoc = np.append(assoc, [company]*len(y))
#         routes = np.append(routes, [route]*len(y))
#         vehicles = np.append(vehicles, [vehicle]*len(y))
#         dates = np.append(dates, [date]*len(y))
#         trips = np.append(trips, [trip]*len(y))

#         lats = np.append(lats, None)
#         lons = np.append(lons, None)
#         names = np.append(names, None)
#         assoc = np.append(assoc, None)
#         routes = np.append(routes, None)
#         vehicles = np.append(vehicles, None)
#         dates = np.append(dates, None)
#         trips = np.append(trips, None)


# lat = lats.tolist()
# lon = lons.tolist()
# date = dates.tolist()
# assoc = assoc.tolist()
# vehicle = vehicles.tolist()
# route = routes.tolist()
# name = names.tolist()
# trip = trips.tolist()

# df = pandas.DataFrame(list(zip(lat, lon,date,assoc,vehicle,route,name,trip)),columns =['lat', 'lon','date','company','vehicleReg','routeName','mapperName','trip id'])
# df = df.set_index('date')
# df = df.dropna()
# df = df.drop_duplicates()