import pandas
import numpy as np
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app

from plotly.subplots import make_subplots
import plotly.express as px


data = pandas.read_csv(r'datasets/cleanedob.csv')
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
                            dcc.RadioItems(id='radiobtn',
                                options=[
                                    {'label': '     Vehicle summaries', 'value': 'demo'},
                                    {'label': '     Route summaries', 'value': 'hh'},
                                    {'label': '     Revenue per kilometer','value':'em'},
                                    #{'label': '     Passengers per hour','value':'cut'},
                                    {'label': '     Distribution','value':'pass'},
                                ],
                                value='demo',className='radio'
                            ),                           
                                           
                        ],width = 3,className='left-side-bar'
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
        Input(component_id = 'radiobtn',component_property = 'value'),
 
        ]

    )
def update_figure(selected_option): #function to update figure each time a new option is selected
    
    if selected_option == 'demo':
        
        fig = make_subplots(rows=4, cols=1)
        table = data.pivot_table(index='vehicle reg no',values='total passengers',aggfunc='sum')
        table = table.sort_values(by='total passengers',ascending=False)
        fig.append_trace({'x':table.index,'y':table['total passengers'],'type':'bar','name':'total passengers'},1,1)
        
        table = data.pivot_table(index='vehicle reg no',values='revenue',aggfunc='sum')
        table = table.sort_values(by='revenue',ascending=False)
        fig.append_trace({'x':table.index,'y':table['revenue'],'type':'bar','name':'revenue per vehicle'},2,1) 
        
        table = data.pivot_table(index='vehicle reg no',values='distance',aggfunc='sum')
        table = table.sort_values(by='distance',ascending=False)
        fig.append_trace({'x':table.index,'y':table['distance'],'type':'bar','name':'distance in km'},3,1) 
        
        table = data.pivot_table(index='vehicle reg no',values='trip id',aggfunc='count')
        table = table.sort_values(by='trip id',ascending=False)
        fig.append_trace({'x':table.index,'y':table['trip id'],'type':'bar','name':'number of trips'},4,1) 
                   
        fig.update_layout(title_text='Vehicle revenue summaries',height=850)

        return fig
        
    elif selected_option == 'hh':
        
        fig = make_subplots(rows=4, cols=1)
        table = data.pivot_table(index='route_id',values='total passengers',aggfunc='sum')
        table = table.sort_values(by='total passengers',ascending=False)
        fig.append_trace({'x':table.index,'y':table['total passengers'],'type':'bar','name':'total passengers'},1,1)
        
        table = data.pivot_table(index='route_id',values='revenue',aggfunc='sum')
        table = table.sort_values(by='revenue',ascending=False)
        fig.append_trace({'x':table.index,'y':table['revenue'],'type':'bar','name':'revenue per vehicle'},2,1) 
        
        table = data.pivot_table(index='route_id',values='distance',aggfunc='sum')
        table = table.sort_values(by='distance',ascending=False)
        fig.append_trace({'x':table.index,'y':table['distance'],'type':'bar','name':'distance in km'},3,1) 
        
        table = data.pivot_table(index='route_id',values='trip id',aggfunc='count')
        table = table.sort_values(by='trip id',ascending=False)
        fig.append_trace({'x':table.index,'y':table['trip id'],'type':'bar','name':'number of trips'},4,1) 
                   
        fig.update_layout(title_text='Vehicle revenue summaries',height=850)

        return fig      
        
    elif selected_option == 'em':
        fig = make_subplots(
            rows=3, cols=2,
            specs=[[{'colspan':2}, {}], #row 1
                [{'colspan':2}, None], #row 2
                [{"colspan": 2}, None], # row 3
                ], #row 5
            print_grid=True,vertical_spacing=0.15)


        table = data.pivot_table(index='vehicle reg no',values='tripRevenueKm',aggfunc='mean').reset_index().sort_values(by='tripRevenueKm',ascending=False)
        fig.append_trace({'x':table['vehicle reg no'],'y':table['tripRevenueKm'],'type':'bar','name':'Average trip earning potential'},1,1)
        
        table = data.pivot_table(index=['vehicle reg no'],values=['revenue','distance'],aggfunc='mean').reset_index()        
        table['vehicleRevenueKm'] = table.revenue/table.distance
        
        #replace inf which comes as a result of speed calculation
        table = table.replace([np.inf, -np.inf], np.nan)
        table = table.fillna(0).sort_values(by='vehicleRevenueKm',ascending=False)
        
        fig.append_trace({'x':table['vehicle reg no'],'y':table['vehicleRevenueKm'],'type':'bar','name':'Total revenue per total distance'},2,1)

        fig.update_layout(margin=dict(l=80,r=20,t=50,b=20),showlegend=True,height=800, title_text="Revenue per kilometer")
        
        return fig      
    
    elif selected_option == 'cut':
        fig = make_subplots(
        rows=1, cols=1,  
        )

        table = data.pivot_table(index='interval',values='total passengers',aggfunc='sum')
        table = table.reset_index()
        table2 = ref.merge(table,on='interval',how='outer')
        table2 = table2.fillna(0)
        table2['axis'] = pandas.to_datetime(table2['interval']).dt.time
        table2 = table2.sort_values(by='axis',ascending=True)

        fig.append_trace({'x':table2['axis'],'y':table2['total passengers'],'type':'scatter','name':'Passenger per 15 min interval'},1,1)
        
        fig.update_layout(margin=dict(l=80,r=20,t=50,b=20),showlegend=True,height=400, title_text="Passengers per 15 min interval")

        return fig
           

    
    else:
        fig = make_subplots(rows=2, cols=3,subplot_titles=("distance", "revenue",'total passengers','number of stops','travel time','speed'))

        fig.append_trace({'y':data.revenue,'type':'box','name':'distance'},1,1)
        fig.append_trace({'y':data.revenue,'type':'box','name':'revenue'},1,2)
        fig.append_trace({'y':data['total passengers'],'type':'box','name':'total passengers'},1,3)

        fig.append_trace({'y':data['number of stops'],'type':'box','name':'number of stops'},2,1)

        fig.append_trace({'y':data.travel_time_min,'type':'box','name':'travel time'},2,2)
        fig.append_trace({'y':data.speed,'type':'box','name':'speed'},2,3)

                    
        fig.update_layout()

        
        return fig        
            
        