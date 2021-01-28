import pandas
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app

from plotly.subplots import make_subplots
import plotly.express as px


data = pandas.read_csv(r'datasets/combinedIntercept.csv')


layout = html.Div([ #canvas

    html.Div( # division for content
        [
            dbc.Row( # row for content
                [
                    dbc.Col( # left column on canvas
                        [
                            
                            dcc.Dropdown(id='cityDemo',
                            options = [{'label': s, 'value': s} for s in sorted(data.city.unique())],
                            value = 'Maseru',
                            style = {'font-size':15,'align':'justify','margin-top':40,'padding':5},
                            placeholder='Select city',
                            clearable=False,

                            ), #fourth element of left column  
                            
                            dcc.RadioItems(id='radiobtn',
                                options=[
                                    {'label': '     Demographic characteristics', 'value': 'demo'},
                                    {'label': '     Household characteristics', 'value': 'hh'},
                                    {'label': '     Employment characteristics','value':'em'},
                                    {'label': '     Current trip characteristics','value':'cut'},
                                    {'label': '     Frequent trip characteristics','value':'ftc'},
                                    {'label': '     Passenger satisfaction','value':'pass'},
                                    {'label': '     Passenger perception','value':'pasp'},
                                    {'label': '     Safety and security','value':'sas'},
                                    {'label': '     Payment characteristics','value':'pay'},
                                    {'label': '     Distributions','value':'dist'},
                                ],
                                value='demo',className='radio'
                            ),                           
                                           


                        ],xs=12,sm=12,md=12,lg=3,xl=3,className='left-side-bar'
                    ), # end of left column on canvas

                    dbc.Col( # right column on canvas
                        [
                            dcc.Graph(id='my-graph2')

                        ],xs=12,sm=12,md=12,lg=9,xl=9

                    ) # end of left column on canvas
                    
                ],style={'height':'100vh'}
                
            ) # end of row for content

        ]
    ), # end of division for content
    

    ]) # end of canvas

@app.callback(
    Output(component_id = 'my-graph2',component_property = "figure"),
    [
        Input(component_id = 'radiobtn',component_property = 'value'),
        Input(component_id = 'cityDemo',component_property = 'value'),

 
        ]

    )
def update_figure(selected_option,cityDemo): #function to update figure each time a new option is selected
    
    data2 = data[data['city']==cityDemo]

    
    if selected_option == 'demo':
        
        fig = make_subplots(
            rows=2, cols=2,
            specs=[[{}, {}], #row 1
                [{'colspan':2}, None], #row 2
                ],
            print_grid=True,vertical_spacing=0.085)        
        
        table = data2.pivot_table(index='gender',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.gender,'y':table['key'],'type':'bar','name':'gender'},1,1)

        table = data2.pivot_table(index='age',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.age,'y':table['key'],'type':'bar','name':'age'},1,2)

        table = data2.pivot_table(index='disability',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.disability,'y':table['key'],'type':'bar','name':'disability'},2,1)
        
        fig.update_layout(margin=dict(l=80,r=20,t=50,b=20),showlegend=True,title_text='Demographic characteristics')  
        
        return fig
        
    elif selected_option == 'hh':
        fig = make_subplots(
            rows=2, cols=2,
            specs=[[{}, {}], #row 1
                [{'colspan':2}, None], #row 2
                ], #row 5
            print_grid=True,vertical_spacing=0.25)

        table = data2.pivot_table(index='household_head_or_member',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.household_head_or_member,'y':table['key'],'type':'bar','name':'household head or member'},1,1)

        table = data2.pivot_table(index='households_own_car',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.households_own_car,'y':table['key'],'type':'bar','name':'household auto ownership'},1,2)

        table = data2.pivot_table(index='num_fam_members',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.num_fam_members,'y':table['key'],'type':'bar','name':'household size'},2,1)

        fig.update_layout(margin=dict(l=80,r=20,t=50,b=20),width=800,showlegend=True, title_text="Household characteristics")
        
        return fig      
        
    elif selected_option == 'em':
        fig = make_subplots(
            rows=3, cols=2,
            specs=[[{'colspan':2}, {}], #row 1
                [{'colspan':2}, None], #row 2
                [{"colspan": 2}, None], # row 3
                ], #row 5
            print_grid=True,vertical_spacing=0.15)

        table = data2.pivot_table(index='employment_status',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.employment_status,'y':table['key'],'type':'bar','name':'employment status'},1,1)

        # table = data.pivot_table(index='specify_employment',values='key',aggfunc='count').reset_index()
        # fig.append_trace({'x':table.specify_employment,'y':table['key'],'type':'bar','name':'specify employment'},2,1)

        table = data2.pivot_table(index='income',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.income,'y':table['key'],'type':'bar','name':'income'},2,1)

        table = data2.pivot_table(index='primary_mode',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.primary_mode,'y':table['key'],'type':'bar','name':'mode'},3,1)

        fig.update_layout(margin=dict(l=80,r=20,t=50,b=20),showlegend=True,height=800, title_text="Employment characteristics")
        
        return fig      
    
    elif selected_option == 'cut':
        fig = make_subplots(
        rows=3, cols=1,  
        )

        table = data2.pivot_table(index='origin',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.origin,'y':table['key'],'type':'bar','name':'origin'},1,1)

        table = data2.pivot_table(index='destination',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.destination,'y':table['key'],'type':'bar','name':'destination'},2,1)

        table = data2.pivot_table(index='trip_frequency',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.trip_frequency,'y':table['key'],'type':'bar','name':'trip_frequency'},3,1)

        fig.update_layout(showlegend=True,height=850,title_text='Current trip characteristics')
        
        return fig
           

    elif selected_option == 'ftc':
        
        fig = make_subplots(
            rows=3, cols=1,
        )

        table = data2.pivot_table(index='commute_most_frequent',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.commute_most_frequent,'y':table['key'],'type':'bar','name':'commute_most_frequent'},1,1)

        table = data2.pivot_table(index='com_most_freq',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.com_most_freq,'y':table['key'],'type':'bar','name':'com_most_freq'},2,1)

        table = data2.pivot_table(index='mode_most_frequent_commute',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.mode_most_frequent_commute,'y':table['key'],'type':'bar','name':'mode_most_frequent_commute'},3,1)

        fig.update_layout(showlegend=True,height=850,title_text='Frequent trip characteristics')
        
        return fig
    elif selected_option == 'pass':
        
        fig = make_subplots(
            rows=4, cols=2,
            specs=[[{}, {}], #row 1
                [{}, {}], #row 2
                [{}, {}], # row 3
                [{}, {}], #row 4
                ],
            print_grid=True, 
        
        )

        table = data2.pivot_table(index='satisfaction_trans_options',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.satisfaction_trans_options,'y':table['key'],'type':'bar','name':'satisfaction_trans_options'},1,1)

        table = data2.pivot_table(index='satisfaction_safety_of_vehicle',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.satisfaction_safety_of_vehicle,'y':table['key'],'type':'bar','name':'satisfaction_safety_of_vehicle'},1,2)

        table = data2.pivot_table(index='satisfaction_safety_of_journey',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.satisfaction_safety_of_journey,'y':table['key'],'type':'bar','name':'satisfaction_safety_of_journey'},2,1)

        table = data2.pivot_table(index='quality',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.quality,'y':table['key'],'type':'bar','name':'quality'},2,2)

        table = data2.pivot_table(index='waiting_times',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.waiting_times,'y':table['key'],'type':'bar','name':'waiting_times'},3,1)

        table = data2.pivot_table(index='location_of_pick_up_and_drop_off',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.location_of_pick_up_and_drop_off,'y':table['key'],'type':'bar','name':'location_of_pick_up_and_drop_off'},3,2)

        table = data2.pivot_table(index='fare',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.fare,'y':table['key'],'type':'bar','name':'fare'},4,1)

        table = data2.pivot_table(index='comfort_on_the_vehicle',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.comfort_on_the_vehicle,'y':table['key'],'type':'bar','name':'comfort_on_the_vehicle'},4,2)

        fig.update_layout(showlegend=True,height=900,title_text='Passenger satisfaction')
        
        return fig
    elif selected_option == 'pasp':
        
        fig = make_subplots(
        rows=3, cols=1,  
        )

        table = data2.pivot_table(index='perception_on_public_transport_likemost',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.perception_on_public_transport_likemost,'y':table['key'],'type':'bar','name':'perception_on_public_transport_likemost'},1,1)

        table = data2.pivot_table(index='perception_on_public_transport_likeleast',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.perception_on_public_transport_likeleast,'y':table['key'],'type':'bar','name':'perception_on_public_transport_likeleast'},2,1)

        table = data2.pivot_table(index='issues_during_trip',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.issues_during_trip,'y':table['key'],'type':'bar','name':'issues_during_trip'},3,1)


        fig.update_layout(showlegend=True,height=900,title_text='Passenger perception')
        
        return fig
    elif selected_option == 'sas':
        fig = make_subplots(
            rows=3, cols=2,
            specs=[[{}, {}], #row 1
                [{'colspan':2}, {}], #row 2
                [{'colspan':2}, {}], # row 3
                ],
            print_grid=True, 
        
        )

        table = data2.pivot_table(index='witnessed_crime',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.witnessed_crime,'y':table['key'],'type':'bar','name':'witnessed_crime'},1,1)

        table = data2.pivot_table(index='sexual_harasment',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.sexual_harasment,'y':table['key'],'type':'bar','name':'sexual_harasment'},1,2)

        table = data2.pivot_table(index='issues_during_trip',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.issues_during_trip,'y':table['key'],'type':'bar','name':'issues_during_trip'},2,1)

        table = data2.pivot_table(index='adhering_to_local_covid_regulations',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.adhering_to_local_covid_regulations,'y':table['key'],'type':'bar','name':'adhering_to_local_covid_regulations'},3,1)

        fig.update_layout(showlegend=True,height=900,title_text='Safety and Security')      
        
        return fig
    
    elif selected_option == 'dist':
        fig = make_subplots(rows=1, cols=3)

        fig.append_trace({'y':data2.trip_travel_time,'type':'box','name':'trip travel time'},1,1)
        fig.append_trace({'y':data2.trip_cost_for_all_modes,'type':'box','name':'trip cost for all modes'},1,2)
        fig.append_trace({'y':data2['cost_all_modes'],'type':'box','name':'cost all modes'},1,3)
        fig.update_layout(showlegend=True)
                    
        return fig  
    else:
        fig = make_subplots(
            rows=1, cols=2,
        )
    
        table = data2.pivot_table(index='cellphone_payment',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.cellphone_payment,'y':table['key'],'type':'bar','name':'cellphone_payment'},1,1)

        table = data2.pivot_table(index='tab_payment',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.tab_payment,'y':table['key'],'type':'bar','name':'tab_payment'},1,2)


        fig.update_layout(showlegend=True,height=400,title_text='Mobile payments')
        
        return fig        
            
        