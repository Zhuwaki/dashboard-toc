import pandas
import plotly.graph_objects as go
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_table
from plotly.subplots import make_subplots

from datetime import datetime as dt

import geopandas as gpd
import shapely.wkt
import shapely.geometry
import numpy as np

from app import app


df = pandas.read_csv(r'datasets/outputformapbox.csv')

df2 = pandas.read_csv(r'datasets/onboard_sample.csv')

df3 = pandas.read_csv(r'datasets/onboard_combined.csv')
#df = df.drop_duplicates()
print(df)
df = df.set_index('date')

# function gets a list of options for drop down and creates a dictionary with label and value
def get_options(drop_down_list):
    dict_list = []
    for i in drop_down_list:
        dict_list.append({'label': i, 'value': i})
    return dict_list


drop_down_list3 = ['Maseru', 'Gaborone', ]

# summaryStats = df3.describe().T
# print(summaryStats)
# summaryStats = summaryStats.drop(['trip id','on/off discrepancy','gps loss (km)','hour'])
# summaryStats = summaryStats.round(0)
# summaryStats = summaryStats.reset_index()
# #summaryStats = summaryStats.drop(['count'])
# #summaryStats = summaryStats.T
# print(summaryStats)

# fig = px.line_mapbox(df,line_group=df['trip id'],lat=df.lat, lon=df.lon, hover_name=df.mapperName,
#                      mapbox_style="carto-positron", zoom=10.7, title='Paratransit network',height=600,color=df.routeName)


layout = html.Div([  # canvas

    html.Div(  # division for content
        [
            dbc.Row(
                [          
                    dbc.Col(
                        
                        [ 
                            dcc.Dropdown(id='drop2',
                            options = [{'label': s, 'value': s} for s in sorted(df.city.unique())],
                            value='Maseru',
                            style={'font-size': 15,
                            'align': 'justify', 'margin': 0,'margin-top':10 }
                            ),
                        ],xs=12,sm=12,md=12,lg=6,xl=6,className='drop-down'
                    ),

                    dbc.Col(
                        [
                            dcc.Dropdown(id='drop-mode',
                            options = [{'label': s, 'value': s} for s in sorted(df.city.unique())],
                            value='Maseru',
                            style={'font-size': 15,
                            'align': 'justify', 'margin': 0,'margin-top':10 }
                            ),
                        ],xs=12,sm=12,md=12,lg=6,xl=6,className='drop-down'
                    )

                ]
            ),
            
            
            dbc.Row(
                [
                    dbc.Col(  # left column on canvas
                        [

  # fourth element of left column

                            html.Div([
                            # dash_table.DataTable(
                            #     id='table',
                            #     columns=[{"id": i, "name": i} 
                            #                 for i in summaryStats.columns.values],
                            #     #data=df2.to_dict('records'),
                            #     style_cell=dict(textAlign='right',padding='2px 22px',border='1px solid black',fontFamily='Arial, Helvetica, sans-serif'),
                            #     style_header=dict(backgroundColor="lavender",fontWeight='bold'),
                            #     style_data=dict(backgroundColor="lavender",padding='2px 22px',border='1px solid black',whiteSpace='normal'),
                            #     style_table=dict(border='1px solid blue',overflowX = 'auto')
                            dcc.Graph(id='barplot',figure={})
                            #     )
                            ]),

                        ], xs=12,sm=12,md=12,lg=6,xl=6,
                            
                    ),

                    dbc.Col(
                        [
                           dcc.Graph(id='mymap2',figure={})
                        ],xs=12,sm=12,md=12,lg=6,xl=6,
                    )
                ],
            ),  # end of row for content

                ]

            ),  # end of row for content
        ]
    ),  # end of division for content


  # end of canvas
  

@app.callback(
    Output('barplot','figure'),
    [
        Input('drop2','value')
    ]
)
def displaytable(cityselect):
    
    dff = df3[df3.city == cityselect]

    fig = make_subplots(rows=2, cols=3)

    fig.append_trace({'y':dff.distance,'type':'box','name':'distance'},1,1)
    fig.append_trace({'y':dff.revenue,'type':'box','name':'revenue'},1,2)
    fig.append_trace({'y':dff['total passengers'],'type':'box','name':'total passengers'},1,3)

    fig.append_trace({'y':dff['number of stops'],'type':'box','name':'number of stops'},2,1)

    fig.append_trace({'y':dff.travel_time_min,'type':'box','name':'travel time'},2,2)
    fig.append_trace({'y':dff.speed,'type':'box','name':'speed'},2,3)

              
    fig.update_layout(showlegend=False,title='Distribution of trip charactersrtics')
   
    return fig

@app.callback(
    Output('mymap2', 'figure'),
    [
        
        Input('drop2', 'value'),
        #Input('my-date-picker-range', 'end_date')
        
    ]
)
def update_output(cityselect):

    
    dff = df[df.city == cityselect]

    fig = px.line_mapbox(dff,line_group=dff['trip id'],lat=dff.lat, lon=dff.lon, hover_name=dff.mapperName,
                     mapbox_style="carto-positron", zoom=10.7, title='Paratransit network',color=dff.routeName)

    # fig=px.density_mapbox(dff, lat = 'LATITUDE', lon = 'LONGITUDE', z = 'APP_SQ_FT', radius = 13, zoom = 10, height = 650,
    #                         center = dict(lat=40.751418, lon=-73.963878), mapbox_style = "carto-positron",
    #                         hover_data = {'BUSINESS_NAME': True, 'LATITUDE': False, 'LONGITUDE': False,
    #                                     'APP_SQ_FT': True})
    return fig
