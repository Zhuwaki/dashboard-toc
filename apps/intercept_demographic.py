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

data = pandas.read_csv(r'C:\Users\nzhuw\Desktop\Data Science Projects\GoAscendal Projects\digital-innovation-maseru\data\processed\Maseru_Clean_data.csv')


fig = make_subplots(
    rows=2, cols=2,
    specs=[[{}, {}], #row 1
           [{'colspan':2}, None], #row 2
          ],
    print_grid=True,vertical_spacing=0.085)

table = data.pivot_table(index='gender',values='key',aggfunc='count').reset_index()
fig.append_trace({'x':table.gender,'y':table['key'],'type':'bar','name':'gender'},1,1)

table = data.pivot_table(index='age',values='key',aggfunc='count').reset_index()
fig.append_trace({'x':table.age,'y':table['key'],'type':'bar','name':'age'},1,2)

table = data.pivot_table(index='disability',values='key',aggfunc='count').reset_index()
fig.append_trace({'x':table.disability,'y':table['key'],'type':'bar','name':'disability'},2,1)

fig.update_layout(margin=dict(l=80,r=20,t=50,b=20),showlegend=True,height=450,title_text='Demographic characteristics')


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
                            # html.P('Select City'
                            # ,style={'font-size':20,'align':'justify','margin':0}), # first element of left column

                            dcc.Dropdown(id='drop',
                            options = get_options(drop_down_list),
                            value = 'Gaborone',
                            placeholder='Select city',
                            style = {'font-size':15,'margin':0}
                            ), #second element of left column

                            dcc.RadioItems(
                                options=[
                                    {'label': 'Demographic characteristics', 'value': 'NYC'},
                                    {'label': 'Household characteristics', 'value': 'MTL'},
                                    {'label': 'Employment characteristics','value':'HHL'},
                                    {'label': 'Current trip characteristics','value':'HHM'},
                                    {'label': 'Frequent trip characteristics','value':'HHN'},
                                    {'label': 'Passenger satisfaction','value':'HHO'},
                                    {'label': 'Passenger perception','value':'HHP'},
                                    {'label': 'Safety and security','value':'HHQ'},
                                    {'label': 'Payments','value':'HHR'},

                              
                                ],
                                value='MTL',className='radio'
                            ),                           
                                           


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