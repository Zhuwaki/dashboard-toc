import pandas
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app



drop_down_list = ['route description','mapper','vehicle reg no','company']

drop_down_list2 = ['Team A','Team B','Team C','Team D','Team E','Team F']

data = pandas.read_csv(r'datasets/dashboard.csv')


def get_options(drop_down_list): # function gets a list of options for drop down and creates a dictionary with label and value
    dict_list = []
    for i in drop_down_list:
        dict_list.append({'label':i,'value':i})
    return dict_list


def long_form(df, product, value): # function prepares the data into long form data - current understanding can only plot long form data
    new_df = df.pivot_table ( index = [product], values = value, aggfunc = 'count' ).reset_index ()
    new_df = new_df.sort_values(by=value,ascending=True)
    new_df = new_df.set_index ( product )
    return new_df



layout = html.Div([ #canvas

    html.Div( # division for content
        [
            dbc.Row( # row for content
                [
                    dbc.Col( # left column on canvas
                        [
                            html.P('Example'
                            ,style={'font-size':20,'align':'justify','margin':30}), # first element of left column

                            dcc.Dropdown(id='drop',
                            options = get_options(drop_down_list),
                            value = 'mapper',
                            placeholder='Please choose report',
                            style = {'font-size':15,'margin':10}
                            ), #second element of left column


                            html.P('Select date range'
                            ,style={'font-size':20,'align':'justify','margin':30}), # third element of left column

                            # dcc.Dropdown(id='drop2',
                            # options = get_options(drop_down_list2),
                            # value = 'Team A',
                            # style = {'font-size':10}
                            # ), #fourth element of left column


                            dcc.DatePickerRange(id='my-date-picker-range',
                                start_date_placeholder_text='Start Period',
                                end_date_placeholder_text='End Period',
                                calendar_orientation = 'horizontal',
                                day_size=39,
                                with_portal=True,
                                minimum_nights = 0,
                                start_date=data['date'].iloc[0],
                                end_date=data['date'].iloc[-1],
                                #persistence = True,
                                #persisted_props=['start_date'],
                                #persistence_type='session',
                                display_format='MMM Do, YYYY',
                                updatemode='singledate',
                                style={'font-size':2,'align':'justify','margin':10}
                            ),

                            # html.Button(
                            #     'Download data',
                            #     id='my-button',
                            #     style={'font-size':16,'align':'justify'}
                            #     ),
                            dbc.Button(
                                'download data',
                                color='info',
                                className='mr-1',
                                outline = True,
                                href='#',
                                style={'font-size':16,'align':'justify','margin':50}
                                )

                        ],width = 3,className='nigel'
                    ), # end of left column on canvas

                    dbc.Col( # right column on canvas
                        [
                            dcc.Graph(id='my-graph3')

                        ],width=9

                    ) # end of left column on canvas
                    
                ],style={'height':'100vh'}
                
            ) # end of row for content

        ]
    ), # end of division for content
    

    ]) # end of canvas

@app.callback(
    Output(component_id = 'my-graph3',component_property = "figure"),
    [

        Input(component_id = 'drop',component_property = 'value'),
        Input('my-date-picker-range', 'start_date'),
        Input('my-date-picker-range', 'end_date'),

        ]

    )
def update_figure(selected_option,start_date,end_date): #function to update figure each time a new option is selected
    value = 'trip id' # key value for longform data function

    dff = data[(data['date']>=start_date) & (data['date']<=end_date)]


    new_df = long_form(dff, selected_option, value) #(input data, selected attribute,value to use in count)

    trace = go.Bar(x = new_df.index, y=new_df[value],marker_color='lightseagreen')

    layout = go.Layout( title = selected_option,xaxis={'title':selected_option},yaxis = {'title':'Total'},
                        barmode = 'stack', height = 500,margin={'b':0})

    fig = go.Figure ( data = [trace], layout = layout )
    fig.update_layout()
    return fig