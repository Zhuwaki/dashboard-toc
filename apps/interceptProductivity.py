import pandas
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

from app import app



drop_down_list = ['username','deviceid']

data = pandas.read_csv(r'datasets/combinedIntercept.csv')

layout = html.Div([ #canvas

    html.Div( # division for content
        [
            dbc.Row( # row for content
                [
                    dbc.Col( # left column on canvas
                        [

                            html.P('Select City'
                            ,style={'font-size':20,'align':'justify','margin':0,'padding':20}), # third element of left column

                            dcc.Dropdown(id='cityProd',
                            options = [{'label': s, 'value': s} for s in sorted(data.city.unique())],
                            value = 'Maseru',
                            style = {'font-size':15,'align':'justify','margin':0,'padding':5}
                            ), #fourth element of left colum
                                 
                            html.P('Select Summary'
                            ,style={'font-size':20,'align':'justify','margin':0,'padding':20}), # first element of left column

                            dcc.Dropdown(id='variableProd',
                            #options = get_options(drop_down_list),
                            value = 'username',
                            placeholder='Please choose report',
                            style = {'font-size':15,'align':'justify','margin':0 ,'padding':5}
                            ), #second element of left column
                            
                            dcc.DatePickerRange(id='my-date-picker-range',
                            start_date_placeholder_text='Start Period',
                            end_date_placeholder_text='End Period',
                            calendar_orientation = 'horizontal',
                            day_size=39,
                            with_portal=True,
                            minimum_nights = 0,
                            start_date=data['submissiondate'].min(),
                            end_date=data['submissiondate'].max(),
                            #persistence = True,
                            #persisted_props=['start_date'],
                            #persistence_type='session',
                            display_format='MMM Do, YYYY',
                            updatemode='singledate',
                            style={'font-size':0,'align':'center','padding':5,'width':205}
                        ), 
   

                        ],xs=12,sm=12,md=12,lg=3,xl=3,className='left-side-bar'
                    ), # end of left column on canvas

                    dbc.Col( # right column on canvas
                        [
                            dcc.Graph(id='my-graph-intercept-productivity')

                        ],xs=12,sm=12,md=12,lg=9,xl=9,

                    ) # end of left column on canvas
                    
                ],
                
                style={'height':'100vh'}
                
            ) # end of row for content

        ]
    ), # end of division for content
    

    ]) # end of canvas




@app.callback(
    Output('variableProd', 'options'),
    [Input('cityProd', 'value')])

def set_route_options(selected_city):
    dff = data[data.city == selected_city]
    return [{'label': i, 'value': i} for i in drop_down_list ]

@app.callback(
    Output(component_id = 'my-graph-intercept-productivity',component_property = "figure"),
    [
        
        Input(component_id = 'cityProd',component_property = 'value'),
        Input(component_id = 'variableProd',component_property = 'value'),


        Input('my-date-picker-range', 'start_date'),
        Input('my-date-picker-range', 'end_date'),

        ]

    )
def update_figure(cityProd,variableProd,start_date,end_date): #function to update figure each time a new option is selected
    value = 'key' # key value for longform data function
    #variable='mapper'
   

    data2 = data[data['city']==cityProd]
    
    dff = data2[(data2['submissiondate']>=start_date) & (data2['submissiondate']<=end_date)]
    
    table = dff.pivot_table(index=variableProd,values=value,aggfunc='count').reset_index()
    table = table.sort_values(by=value,ascending=False)
    
    fig = px.bar(data_frame=table,x=variableProd,y='key',text='key',title=variableProd,color='key')
    fig.update_layout(uniformtext_minsize=6, uniformtext_mode='show')
    fig.update_layout()
    return fig