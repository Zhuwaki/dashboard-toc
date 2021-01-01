import pandas
import plotly.graph_objects as go
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from datetime import datetime as dt

import geopandas as gpd
import shapely.wkt
import shapely.geometry
import numpy as np

from app import app

from mapboxdata import df

# function gets a list of options for drop down and creates a dictionary with label and value
def get_options(drop_down_list):
    dict_list = []
    for i in drop_down_list:
        dict_list.append({'label': i, 'value': i})
    return dict_list


drop_down_list3 = ['Maseru', 'Gaborone', ]


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




layout = html.Div([  # canvas

    html.Div(  # division for content
        [

            dbc.Row(
                [
                    dbc.Col(  # left column on canvas
                        [

                            dcc.Dropdown(id='drop2',
                            options=get_options(drop_down_list3),
                            value='Maseru',
                            style={'font-size': 15,
                                'align': 'justify', 'margin': 5,'width':286,'margin-top':60 }
                            ),  # fourth element of left column

                            dcc.DatePickerRange(id='my-date-picker-range',
                                start_date_placeholder_text='Start Period',
                                end_date_placeholder_text='End Period',
                                calendar_orientation='horizontal',
                                day_size=39,
                                with_portal=True,
                                minimum_nights=0,
                                start_date=dt(2020, 12, 1).date(),
                                end_date=dt(2021, 1, 1).date(),
                                # persistence = True,
                                # persisted_props=['start_date'],
                                # persistence_type='session',
                                display_format='MMM Do, YYYY',
                                updatemode='singledate',
                                style={'font-size': 2,
                                    'align': 'left', 'margin': 10}
                            )

                        ], width=3
                            
                    ),

                    dbc.Col(
                        [
                           dcc.Graph(id='mymap2')
                        ],width=9
                    )
                ]
            ),  # end of row for content

                ]

            ),  # end of row for content
        ]
    ),  # end of division for content


  # end of canvas

@app.callback(
    Output('mymap2', 'figure'),
    [Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date')]
)
def update_output(start_date, end_date):
    # print("Start date: " + start_date)
    # print("End date: " + end_date)
    dff=df.loc[start_date:end_date]
    # print(dff[:5])
    
    fig = px.line_mapbox(dff,line_group=dff['trip id'],lat=dff.lat, lon=dff.lon, hover_name=dff.mapperName,
                     mapbox_style="stamen-terrain", zoom=10.7, title='Paratransit network',height=600,color=dff.vehicleReg)

    # fig=px.density_mapbox(dff, lat = 'LATITUDE', lon = 'LONGITUDE', z = 'APP_SQ_FT', radius = 13, zoom = 10, height = 650,
    #                         center = dict(lat=40.751418, lon=-73.963878), mapbox_style = "carto-positron",
    #                         hover_data = {'BUSINESS_NAME': True, 'LATITUDE': False, 'LONGITUDE': False,
    #                                     'APP_SQ_FT': True})
    return fig
