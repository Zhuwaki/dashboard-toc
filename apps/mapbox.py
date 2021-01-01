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
print(df)

# function gets a list of options for drop down and creates a dictionary with label and value
def get_options(drop_down_list):
    dict_list = []
    for i in drop_down_list:
        dict_list.append({'label': i, 'value': i})
    return dict_list


drop_down_list3 = ['Maseru', 'Gaborone', ]



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
                                start_date=dt(2020, 12, 9).date(),
                                end_date=dt(2020, 12, 31).date(),
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
                     mapbox_style="stamen-terrain", zoom=10.7, title='Paratransit network',height=600)

    # fig=px.density_mapbox(dff, lat = 'LATITUDE', lon = 'LONGITUDE', z = 'APP_SQ_FT', radius = 13, zoom = 10, height = 650,
    #                         center = dict(lat=40.751418, lon=-73.963878), mapbox_style = "carto-positron",
    #                         hover_data = {'BUSINESS_NAME': True, 'LATITUDE': False, 'LONGITUDE': False,
    #                                     'APP_SQ_FT': True})
    return fig
