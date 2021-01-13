import pandas
import numpy as np
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash

from app import app

from plotly.subplots import make_subplots
import plotly.express as px


data = pandas.read_csv(r'datasets/combined_mode_cleanedob.csv')
data['interval'] = pandas.to_datetime(data['interval'])
ref = pandas.read_csv(r'datasets/15_min_interval.csv')

ref['interval'] = pandas.to_datetime(ref['interval'])


data['tripRevenueKm'] = data['revenue']/data['distance']
#replace inf which comes as a result of speed calculation
data = data.replace([np.inf, -np.inf], np.nan)
data = data.fillna(0)

layout = html.Div([ #canvas

    html.Div( # division for content
        [
            dbc.Row( # row for content
                [
                    dbc.Col( # left column on canvas
                        [ 
                            html.Div(
                                [
                                    html.P('Route Passenger Demand')
                                ],
                                className='summary-survey'
                            ),
                            
                            
                            html.Label('Select city'
                            ,style={'font-size':20,'align':'justify','margin':0,'padding':10}), # first element of left column
                            dcc.Dropdown(id='city',
                            options = [{'label': s, 'value': s} for s in sorted(data.city.unique())],
                            value = 'Maseru',
                            style = {'font-size':15,'align':'justify','margin':0,'padding':5},
                            placeholder='Select city',
                            clearable=False,

                            ), #fourth element of left column  
                            
                            
                            html.Label('Select route'
                            ,style={'font-size':20,'align':'justify','margin':0,'padding':10}), # first element of left column
                            dcc.Dropdown(id='route',
                            options = [],
                            style = {'font-size':15,'align':'justify','margin':0,'padding':5},
                            placeholder='Select route',
                            multi=True,
                            ), #fourth element of left column 
                            
                            html.Label('Select date'
                            ,style={'font-size':20,'align':'justify','margin':0,'padding':10}), # first element of left column
                            dcc.DatePickerRange(id='my-date-picker-range',
                            start_date_placeholder_text='Start Period',
                            end_date_placeholder_text='End Period',
                            calendar_orientation = 'horizontal',
                            day_size=39,
                            with_portal=True,
                            minimum_nights = 0,
                            start_date=data['date mapped'].min(),
                            end_date=data['date mapped'].max(),
                            #persistence = True,
                            #persisted_props=['start_date'],
                            #persistence_type='session',
                            display_format='MMM Do, YYYY',
                            updatemode='singledate',
                            style={'font-size':2,'align':'center','padding':5,'width':205}
                        ), 
                                          
                        ],xs=12,sm=12,md=12,lg=3,xl=3,className='left-side-bar'
                        
                        
                    ), # end of left column on canvas

                    dbc.Col( # right column on canvas
                        [
                            dcc.Graph(id='my-graph4',figure={})

                        ],xs=12,sm=12,md=12,lg=9,xl=9

                    ) # end of left column on canvas
                    
                ],style={'height':'100vh'}
                
            ) # end of row for content

        ]
    ), # end of division for content
    

    ]) # end of canvas


@app.callback(
    Output('route', 'options'),
    [Input('city', 'value')])

def set_route_options(selected_city):
    dff = data[data.city == selected_city]
    return [{'label': i, 'value': i} for i in sorted(dff.route_id.unique())]


@app.callback(
    Output('route', 'value'),
    [Input('route', 'options')])

def set_route_value(available_options):
    print(available_options)
    return [x['value'] for x in available_options]


@app.callback(
    Output(component_id = 'my-graph4',component_property = "figure"),
    [
        Input(component_id = 'city',component_property = 'value'),
        
        Input(component_id ='route', component_property ='value'),
        
        Input('my-date-picker-range', 'start_date'),
        Input('my-date-picker-range', 'end_date'),
        ]
    )
def update_figure(city,route,start_date,end_date): #function to update figure each time a new option is selected
    
    data2 = data[(data['date mapped']>=start_date) & (data['date mapped']<=end_date)]
    print(data2.shape)

    
    fig = make_subplots(rows=1, cols=1,)
 
    if len(route) == 0 :
        return {'data':[]}
    
    else:
        
        dff = data2[(data2['city']==city) & (data2.route_id.isin(route))]
        
        table = dff.pivot_table(index='interval',values='total passengers',aggfunc='sum')
        table = table.reset_index()
        table2 = ref.merge(table,on='interval',how='outer')
        table2 = table2.fillna(0)
        table2['axis'] = pandas.to_datetime(table2['interval']).dt.time
        table2 = table2.sort_values(by='axis',ascending=True)

        fig.append_trace({'x':table2['axis'],'y':table2['total passengers'],'type':'scatter','name':'Passenger per 15 min interval'},1,1)
        
        fig.update_layout(title_text="Passengers per 15 min interval")
        
        return fig


        