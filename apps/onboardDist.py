import pandas
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_table



from plotly.subplots import make_subplots
import plotly.express as px

from app import app

data = pandas.read_csv((r'datasets/combined_mode_cleanedob.csv'))

summaryStats = data.describe().T

summaryStats = summaryStats.drop(['trip id','on/off discrepancy','gps loss (km)','hour'])

#print(summaryStats)
summaryStats = summaryStats.reset_index()

summaryStats = summaryStats.round(0)

#fig = make_subplots(rows=2, cols=3,subplot_titles=("distance", "revenue",'total passengers','number of stops','travel time','speed'))
fig = make_subplots(rows=2, cols=3)

fig.append_trace({'y':data.distance,'type':'box','name':'distance'},1,1)
fig.append_trace({'y':data.revenue,'type':'box','name':'revenue'},1,2)
fig.append_trace({'y':data['total passengers'],'type':'box','name':'total passengers'},1,3)

fig.append_trace({'y':data['number of stops'],'type':'box','name':'number of stops'},2,1)

fig.append_trace({'y':data.travel_time_min,'type':'box','name':'travel time'},2,2)
fig.append_trace({'y':data.speed,'type':'box','name':'speed'},2,3)

              
fig.update_layout(showlegend=False)



drop_down_list = ['route description','mapper','vehicle reg no','company']

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
                            dcc.Dropdown(id='drop4',
                            options = get_options(drop_down_list),
                            value = 'mapper',
                            placeholder='Please choose report',
                            style = {'font-size':15,'margin':0}
                            ), #second element of left column                            

                            dcc.RadioItems(
                                options=[
                                    {'label': 'Histogram', 'value': 'NYC'},
                                    {'label': 'Boxplot', 'value': 'MTL'},
                                ],
                                value='MTL',className='radio'
                            ),                           
                                                                           

                        ],width = 3,className='left-side-bar'
                    ), # end of left column on canvas
                    
                    
                    dbc.Col( # right column on canvas
                        [
                            dcc.Graph(id='my-graph',figure=fig),
                            #html.Img(src=app.get_asset_url('method.png'),style={'margin-top':1,'margin-left':0, 'width':'100%'}),


                        ],width=9

                    ), # end of left column on canvas


                    dbc.Col( # right column on canvas
                        [
                            #dcc.Graph(id='my-graph',figure=fig),
                            #html.Img(src=app.get_asset_url('method.png'),style={'margin-top':1,'margin-left':0, 'width':'100%'}),
                            # html.Div([
                            # dash_table.DataTable(
                            #     id='table',
                            #     columns=[{"name": i, "id": i} 
                            #                 for i in summaryStats.columns],
                            #     data=summaryStats.to_dict('records'),
                            #     style_cell=dict(textAlign='right',padding='2px 22px',border='1px solid black',fontFamily='Open Sans'),
                            #     style_header=dict(backgroundColor="lavender",fontWeight='bold'),
                            #     style_data=dict(backgroundColor="lavender",padding='2px 22px',border='1px solid black',whiteSpace='normal'),
                            #     #style_table=dict(border='1px solid blue')
                            #     )
                            # ],className='table'),


                        ],width=0

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