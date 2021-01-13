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


mapboxData = pandas.read_csv(r'datasets/mapbox_trips_output.csv')


onboardData = pandas.read_csv(r'datasets/combined_mode_cleanedob.csv')


layout = html.Div([  # canvas

    html.Div(  # division for content
        [
            dbc.Row(
                [          
                    dbc.Col(
                        
                        [ 
                            dcc.Dropdown(id='drop-city',
                            options = [{'label': s, 'value': s} for s in sorted(mapboxData.city.unique())],
                            value = mapboxData.city.unique()[1],
                            style={'font-size': 15,
                            'align': 'justify', 'margin': 0,'margin-top':10 }
                            ),
                        ],xs=12,sm=12,md=12,lg=6,xl=5,className='drop-down'
                    ),

                    dbc.Col(
                        [
                            dcc.Dropdown(id='drop-mode',
                            options = [{'label': s, 'value': s} for s in sorted(mapboxData['vehicle type'].unique())],
                            value = ['Mini-bus'],
                            multi = True,
                            style={'font-size': 15,
                            'align': 'justify', 'margin': 0,'margin-top':10 }
                            ),
                        ],xs=12,sm=12,md=12,lg=6,xl=7,className='drop-down'
                    )

                ]
            ),
            
            
            dbc.Row(
                [
                    dbc.Col(  # left column on canvas
                        [

  # fourth element of left column

                            html.Div([

                            dcc.Graph(id='graph',figure={})
                            #     )
                            ]),

                        ], xs=12,sm=12,md=12,lg=6,xl=5,
                            
                    ),

                    dbc.Col(
                        [
                           dcc.Graph(id='mymap2',figure={})
                        ],xs=12,sm=12,md=12,lg=6,xl=7,
                    )
                ],
            ),  # end of row for content

                ]

            ),  # end of row for content
        ]
    ),  # end of division for content


  # end of canvas
 
 
@app.callback(
    Output('graph','figure'),
    [
        Input('drop-city','value'),
        Input('drop-mode', 'value')  

    ]
)

def displaytable(cityselect,mode):
    
    dff = onboardData[onboardData.city == cityselect]
    dff = dff[dff['vehicle type'].isin(mode)]

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
        
        Input('drop-city', 'value'),
        Input('drop-mode', 'value')  
    ]
)

def update_output(cityselect,mode):

    if len(mode) == 0:
        
        return {'data':[]}
    else:
        dff = mapboxData[mapboxData.city == cityselect]
        
        dff = dff[dff['vehicle type'].isin(mode)]
        

        fig = px.line_mapbox(dff,line_group=dff['trip id'],lat=dff.lat, lon=dff.lon, hover_name=dff.mapperName,
                        mapbox_style="carto-positron", zoom=10.7, title='Paratransit network',color='routeName')

        return fig


