import pandas
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app



drop_down_list = ['route_id','mapper','vehicle reg no','company']
data = pandas.read_csv(r'datasets/combined_mode_cleanedob.csv')


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
                            ,style={'font-size':20,'align':'justify','margin':0,'padding':20}), # third element of left column

                            dcc.Dropdown(id='city',
                            options = [{'label': s, 'value': s} for s in sorted(data.city.unique())],
                            value = 'Maseru',
                            style = {'font-size':15,'align':'justify','margin':0,'padding':5}
                            ), #fourth element of left colum
                            
                            
                            dcc.Dropdown(id='vehicle-type',
                            options = [{'label': s, 'value': s} for s in sorted(data['vehicle type'].unique())],
                            value = ['4+1'],
                            multi=True,
                            style = {'font-size':15,'align':'justify','margin':0,'padding':5}
                            ), #fourth element of left colum
                                 
                            html.P('Select Summary'
                            ,style={'font-size':20,'align':'justify','margin':0,'padding':20}), # first element of left column

                            dcc.Dropdown(id='variable',
                            #options = get_options(drop_down_list),
                            value = 'mapper',
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
                            start_date=data['date mapped'].min(),
                            end_date=data['date mapped'].max(),
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
                            dcc.Graph(id='my-graph')

                        ],xs=12,sm=12,md=12,lg=9,xl=9,

                    ) # end of left column on canvas
                    
                ],
                
                style={'height':'100vh'}
                
            ) # end of row for content

        ],style={'overflow-x':'hidden','width':'100vw','height':'100vh'}
    ), # end of division for content
    

    ]) # end of canvas




@app.callback(
    Output('variable', 'options'),
    [Input('city', 'value')])

def set_route_options(selected_city):
    dff = data[data.city == selected_city]
    return [{'label': i, 'value': i} for i in drop_down_list ]

@app.callback(
    Output(component_id = 'my-graph',component_property = "figure"),
    [
        
        Input(component_id = 'city',component_property = 'value'),
        Input(component_id = 'variable',component_property = 'value'),
        

        Input('my-date-picker-range', 'start_date'),
        Input('my-date-picker-range', 'end_date'),
        
        Input(component_id = 'vehicle-type',component_property = 'value'),


        ]

    )
def update_figure(city,variable,start_date,end_date,mode): #function to update figure each time a new option is selected
    value = 'trip id' # key value for longform data function
    #variable='mapper'
    print(start_date)
    
    if variable == None :
        
        return {'data':[]}
    
    elif start_date < data['date mapped'].min():
        
        return {'data':[]}
    
    elif end_date > data['date mapped'].max():
            
        return {'data':[]}
    
    elif len(mode)==0:
        return{'data':[]}
        
    else:

        data2 = data[data['city']==city]
        
        data2 = data2[data2['vehicle type'].isin(mode)]
        
        print(data2)
        
        dff = data2[(data2['date mapped']>=start_date) & (data2['date mapped']<=end_date)]
        
        table = dff.pivot_table(index=variable,values='trip id',aggfunc='count').reset_index()
        table = table.sort_values(by=value,ascending=False)
        
        trace = go.Bar(x = table[variable], y=table['trip id'],marker_color='lightseagreen')

        layout = go.Layout( title = variable,xaxis={'title':variable},yaxis = {'title':'Total'},
                            barmode = 'stack', height = 500,margin={'b':0})

        fig = go.Figure ( data = [trace], layout = layout )
        fig.update_layout()
        return fig