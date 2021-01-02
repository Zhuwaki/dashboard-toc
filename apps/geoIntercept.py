import pandas
import plotly.graph_objects as go
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_table

from datetime import datetime as dt

import geopandas as gpd
import shapely.wkt
import shapely.geometry
import numpy as np

from app import app

#from mapboxdata import df

df = pandas.read_csv(r'datasets/Intercept_Arusha.csv')
df2 = pandas.read_csv(r'datasets/sample.csv')
print(df2)


df = df[['SubmissionDate','geolocation-Latitude','geolocation-Longitude','gender']]
df = df.dropna()
#df = df.drop_duplicates()
print(df)
#df = df.set_index('date')

# function gets a list of options for drop down and creates a dictionary with label and value
def get_options(drop_down_list):
    dict_list = []
    for i in drop_down_list:
        dict_list.append({'label': i, 'value': i})
    return dict_list

# def generate_table(dataframe, max_rows=3):
#     return html.Table(
#         # Header
#         [html.Tr([html.Th(col) for col in dataframe.columns]) ] +
#         # Body
#         [html.Tr([
#             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#         ]) for i in range(min(len(dataframe), max_rows))], style={'border':'5px', 'font-size':'1.2rem'}
#     )

drop_down_list3 = ['Maseru', 'Gaborone', ]

fig = px.scatter_mapbox(df,lat=df['geolocation-Latitude'], lon=df['geolocation-Longitude'],
                     mapbox_style="carto-positron", zoom=10.7, title='Location of Intercept Surveys',color="gender",height=600)


# fig2 = go.Figure(data=[go.Table(
#     header=dict(values=list(df2.columns),
#                 fill_color='paleturquoise',
#                 align='left'),
#     cells=dict(values=[df2.variable, df2.target, df2.actual, df2.diff],
#                fill_color='lavender',
#                align='left'))
# ])


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
                                'align': 'justify', 'margin': 0,'margin-top':60 }
                            ),  # fourth element of left column

                            # dcc.DatePickerRange(id='my-date-picker-range',
                            #     start_date_placeholder_text='Start Period',
                            #     end_date_placeholder_text='End Period',
                            #     calendar_orientation='horizontal',
                            #     day_size=39,
                            #     with_portal=True,
                            #     minimum_nights=0,
                            #     start_date=dt(2020, 12, 9).date(),
                            #     end_date=dt(2020, 12, 31).date(),
                            #     # persistence = True,
                            #     # persisted_props=['start_date'],
                            #     # persistence_type='session',
                            #     display_format='MMM Do, YYYY',
                            #     updatemode='singledate',
                            #     style={'font-size': 2,
                            #         'align': 'left', 'margin': 10}
                            # )
                            html.Div([
                            dash_table.DataTable(
                                id='table',
                                columns=[{"name": i, "id": i} 
                                            for i in df2.columns],
                                data=df2.to_dict('records'),
                                style_cell=dict(textAlign='right',padding='2px 22px',border='1px solid black',fontFamily='Open Sans'),
                                style_header=dict(backgroundColor="paleturquoise",fontWeight='bold'),
                                style_data=dict(backgroundColor="lavender",padding='2px 22px',border='1px solid black',whiteSpace='normal'),
                                #style_table=dict(border='1px solid blue')
                                )
                            ],className='table'),
                            
                            #dcc.Graph(id='table',figure=fig2)
                           # html.Img(src=app.get_asset_url('GoMetro-2.png'),style={'margin-top':300,'margin-left':80, 'width':'20%'})
                        #    html.H4(children='Sampling',style={'margin-top':30,'margin-left':0}),
                        #    generate_table(df2)
                        

                        ], width=3,className='nigel'
                            
                    ),

                    dbc.Col(
                        [
                           dcc.Graph(id='mymap3',figure=fig)
                        ],width=9
                    )
                ],style={'height':'100vh'}
            ),  # end of row for content

                ]

            ),  # end of row for content
        ]
    ),  # end of division for content


  # end of canvas

# @app.callback(
#     Output('mymap2', 'figure'),
#     [Input('my-date-picker-range', 'start_date'),
#      Input('my-date-picker-range', 'end_date')]
# )
# def update_output(start_date, end_date):
#     # print("Start date: " + start_date)
#     # print("End date: " + end_date)
#     dff=df.loc[start_date:end_date]
#     # print(dff[:5])
    
#     fig = px.line_mapbox(dff,line_group=dff['trip id'],lat=dff.lat, lon=dff.lon, hover_name=dff.mapperName,
#                      mapbox_style="carto-positron", zoom=10.7, title='Paratransit network',height=600,color=dff.routeID)

#     # fig=px.density_mapbox(dff, lat = 'LATITUDE', lon = 'LONGITUDE', z = 'APP_SQ_FT', radius = 13, zoom = 10, height = 650,
#     #                         center = dict(lat=40.751418, lon=-73.963878), mapbox_style = "carto-positron",
#     #                         hover_data = {'BUSINESS_NAME': True, 'LATITUDE': False, 'LONGITUDE': False,
#     #                                     'APP_SQ_FT': True})
#     return fig
