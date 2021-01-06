import pandas
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app

from plotly.subplots import make_subplots
import plotly.express as px



drop_down_list = ['route description','mapper','vehicle reg no','company']

drop_down_list2 = ['Team A','Team B','Team C','Team D','Team E','Team F']

#data = pandas.read_csv(r'datasets/dashboard.csv')

data = pandas.read_csv(r'datasets/Maseru_Clean_data.csv')


fig = make_subplots(rows=1, cols=3)

fig.append_trace({'y':data.trip_travel_time,'type':'box','name':'trip travel time'},1,1)
fig.append_trace({'y':data.trip_cost_for_all_modes,'type':'box','name':'trip cost for all modes'},1,2)
fig.append_trace({'y':data['cost_all_modes'],'type':'box','name':'cost all modes'},1,3)
fig.update_layout(showlegend=True)


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
                            html.P('Select City'
                            ,style={'font-size':20,'align':'justify','margin':0}), # first element of left column

                            dcc.Dropdown(id='drop',
                            options = get_options(drop_down_list),
                            value = 'mapper',
                            placeholder='Please choose report',
                            style = {'font-size':15,'margin':0}
                            ), #second element of left column

                            # html.P('Demographics'
                            # ,style={'font-size':20,'align':'justify','margin':0}), # third element of left column
                            
                            # dcc.Dropdown(id='drop2',
                            # options = get_options(drop_down_list),
                            # value = 'mapper',
                            # placeholder='Please choose report',
                            # style = {'font-size':15,'margin':0}
                            # ), #second element of left column                            
                            
                            # html.P('Current trip'
                            # ,style={'font-size':20,'align':'justify','margin':0}), # third element of left column
                            # dcc.Dropdown(id='drop',
                            # options = get_options(drop_down_list),
                            # value = 'mapper',
                            # placeholder='Please choose report',
                            # style = {'font-size':15,'margin':0}
                            # ), #second element of left column 
                            dcc.RadioItems(
                                options=[
                                    {'label': 'Histogram', 'value': 'NYC'},
                                    {'label': 'Boxplot', 'value': 'MTL'},
                                ],
                                value='MTL',className='radio'
                            ),                           
                                           
                            # html.P('Most frequent trip'
                            # ,style={'font-size':20,'align':'justify','margin':0}), # third element of left column
                            # dcc.Dropdown(id='drop',
                            # options = get_options(drop_down_list),
                            # value = 'mapper',
                            # placeholder='Please choose report',
                            # style = {'font-size':15,'margin':0}
                            # ), #second element of left column                            
                            # html.P('Passenger satisfaction'
                            # ,style={'font-size':20,'align':'justify','margin':0}), # third element of left column
                            # dcc.Dropdown(id='drop',
                            # options = get_options(drop_down_list),
                            # value = 'mapper',
                            # placeholder='Please choose report',
                            # style = {'font-size':15,'margin':0}
                            # ), #second element of left column                            
                            # html.P('Passenger perception'
                            # ,style={'font-size':20,'align':'justify','margin':0}), # third element of left column 
                            # dcc.Dropdown(id='drop',
                            # options = get_options(drop_down_list),
                            # value = 'mapper',
                            # placeholder='Please choose report',
                            # style = {'font-size':15,'margin':0}
                            # ), #second element of left column                             
                            # html.P('Safety and security'
                            # ,style={'font-size':20,'align':'justify','margin':0}), # third element of left column    
                            # dcc.Dropdown(id='drop',
                            # options = get_options(drop_down_list),
                            # value = 'mapper',
                            # placeholder='Please choose report',
                            # style = {'font-size':15,'margin':0}
                            # ), #second element of left column                            
                            # html.P('Payments'
                            # ,style={'font-size':20,'align':'justify','margin':0}), # third element of left column                                                       
                            #  dcc.Dropdown(id='drop',
                            # options = get_options(drop_down_list),
                            # value = 'mapper',
                            # placeholder='Please choose report',
                            # style = {'font-size':15,'margin':0}
                            # ), #second element of left column                                                        

                            # # dcc.Dropdown(id='drop2',
                            # # options = get_options(drop_down_list2),
                            # # value = 'Team A',
                            # # style = {'font-size':10}
                            # # ), #fourth element of left column


                            # # dcc.DatePickerRange(id='my-date-picker-range',
                            # #     start_date_placeholder_text='Start Period',
                            # #     end_date_placeholder_text='End Period',
                            # #     calendar_orientation = 'horizontal',
                            # #     day_size=39,
                            #     with_portal=True,
                            #     minimum_nights = 0,
                            #     start_date=data['date'].iloc[0],
                            #     end_date=data['date'].iloc[-1],
                            #     #persistence = True,
                            #     #persisted_props=['start_date'],
                            #     #persistence_type='session',
                            #     display_format='MMM Do, YYYY',
                            #     updatemode='singledate',
                            #     style={'font-size':2,'align':'justify','margin':10}
                            # ),

                            # html.Button(
                            #     'Download data',
                            #     id='my-button',
                            #     style={'font-size':16,'align':'justify'}
                            #     ),
                            # dbc.Button(
                            #     'download data',
                            #     color='info',
                            #     className='mr-1',
                            #     outline = True,
                            #     href='#',
                            #     style={'font-size':16,'align':'justify','margin':50}
                            #     )

                        ],width = 3,className='left-side-bar'
                    ), # end of left column on canvas

                    dbc.Col( # right column on canvas
                        [
                            dcc.Graph(id='my-graph2',figure=fig)

                        ],width=9

                    ) # end of left column on canvas
                    
                ],style={'height':'100vh'}
                
            ) # end of row for content

        ]
    ), # end of division for content
    

    ]) # end of canvas

# @app.callback(
#     Output(component_id = 'my-graph2',component_property = "figure"),
#     [

#         Input(component_id = 'drop',component_property = 'value'),
#         Input('my-date-picker-range', 'start_date'),
#         Input('my-date-picker-range', 'end_date'),

#         ]

#     )
# def update_figure(selected_option,start_date,end_date): #function to update figure each time a new option is selected
#     value = 'trip id' # key value for longform data function

#     dff = data[(data['date']>=start_date) & (data['date']<=end_date)]


#     new_df = long_form(dff, selected_option, value) #(input data, selected attribute,value to use in count)

#     trace = go.Bar(x = new_df.index, y=new_df[value],marker_color='lightseagreen')

#     layout = go.Layout( title = selected_option,xaxis={'title':selected_option},yaxis = {'title':'Total'},
#                         barmode = 'stack', height = 500,margin={'b':0})

#     fig = go.Figure ( data = [trace], layout = layout )
#     fig.update_layout()
#     return fig