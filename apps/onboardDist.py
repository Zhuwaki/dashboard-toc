import pandas
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from plotly.subplots import make_subplots
import plotly.express as px

from app import app

data = pandas.read_csv((r'C:\Users\nzhuw\Desktop\Data Science Projects\GoAscendal Projects\digital-innovation-maseru\models\cleanedob.csv'))

#fig = make_subplots(rows=1, cols=2,subplot_titles=("Plot 1", "Plot 2"))

# fig = px.box(data_frame=data,y='distance')
# fig2 = px.box(data_frame=data,y='revenue')
# fig3 = px.box(data_frame=data,y='total passengers')
#fig.add_trace(px.box(data, y='distance'))

# fig.add_trace(px.box(data, y='speed',row=1, col=2))


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
                            
                            html.Div(
                                [
                                    html.H6('Onboard summary statistics')
                                ],
                                className='summary-survey'
                            ),                

                        ],width = 3,className='left-side-bar'
                    ), # end of left column on canvas

                    dbc.Col( # right column on canvas
                        [
                            #dcc.Graph(id='my-graph',figure=fig3)
                            #html.Img(src=app.get_asset_url('method.png'),style={'margin-top':1,'margin-left':0, 'width':'100%'}),


                        ],width=3

                    ), # end of left column on canvas
                    dbc.Col( # right column on canvas
                        [
                            #dcc.Graph(id='my-graph',figure=fig2)
                            #html.Img(src=app.get_asset_url('method.png'),style={'margin-top':1,'margin-left':0, 'width':'100%'}),


                        ],width=3

                    ), # end of left column on canvas
                    dbc.Col( # right column on canvas
                        [
                            #dcc.Graph(id='my-graph',figure=fig),
                            #html.Img(src=app.get_asset_url('method.png'),style={'margin-top':1,'margin-left':0, 'width':'100%'}),


                        ],width=3

                    ), # end of left column on canvas
                    
                    
                    
                ],
                
                style={'height':'100vh','width':'100%'}
                
            ) # end of row for content

        ]
    ), # end of division for content
    

    ]) # end of canvas

# @app.callback(
#     Output(component_id = 'my-graph',component_property = "figure"),
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