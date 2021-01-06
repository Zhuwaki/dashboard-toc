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

                            # dcc.Dropdown(id='drop',
                            # options = get_options(drop_down_list),
                            # value = 'Gaborone',
                            # placeholder='Select city',
                            # style = {'font-size':15,'margin':0}
                            # ), #second element of left column

                            dcc.RadioItems(id='radiobtn',
                                options=[
                                    {'label': 'Demographic characteristics', 'value': 'demo'},
                                    {'label': 'Household characteristics', 'value': 'hh'},
                                    {'label': 'Employment characteristics','value':'em'},
                                    {'label': 'Current trip characteristics','value':'cut'},
                                    {'label': 'Frequent trip characteristics','value':'ftc'},
                                    {'label': 'Passenger satisfaction','value':'pass'},
                                    {'label': 'Passenger perception','value':'pasp'},
                                    {'label': 'Safety and security','value':'sas'},
                                    {'label': 'Payments','value':'pay'},
                              
                                ],
                                value='pay',className='radio'
                            ),                           
                                           


                        ],width = 3,className='left-side-bar'
                    ), # end of left column on canvas

                    dbc.Col( # right column on canvas
                        [
                            dcc.Graph(id='my-graph2')

                        ],width=9

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

        #Input(component_id = 'drop',component_property = 'value'),
 
        ]

    )
def update_figure(selected_option): #function to update figure each time a new option is selected
    value = 'trip id' # key value for longform data function

#    dff = data[(data['date']>=start_date) & (data['date']<=end_date)]
    
    dff= data
    
    if selected_option == 'demo':
        
        fig = make_subplots(
            rows=2, cols=2,
            specs=[[{}, {}], #row 1
                [{'colspan':2}, None], #row 2
                ],
            print_grid=True,vertical_spacing=0.085)        
        
        table = dff.pivot_table(index='gender',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.gender,'y':table['key'],'type':'bar','name':'gender'},1,1)

        table = data.pivot_table(index='age',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.age,'y':table['key'],'type':'bar','name':'age'},1,2)

        table = data.pivot_table(index='disability',values='key',aggfunc='count').reset_index()
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

        table = data.pivot_table(index='household_head_or_member',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.household_head_or_member,'y':table['key'],'type':'bar','name':'household head or member'},1,1)

        table = data.pivot_table(index='households_own_car',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.households_own_car,'y':table['key'],'type':'bar','name':'household auto ownership'},1,2)

        table = data.pivot_table(index='num_fam_members',values='key',aggfunc='count').reset_index()
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

        table = data.pivot_table(index='employment_status',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.employment_status,'y':table['key'],'type':'bar','name':'employment status'},1,1)

        # table = data.pivot_table(index='specify_employment',values='key',aggfunc='count').reset_index()
        # fig.append_trace({'x':table.specify_employment,'y':table['key'],'type':'bar','name':'specify employment'},2,1)

        table = data.pivot_table(index='income',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.income,'y':table['key'],'type':'bar','name':'income'},2,1)

        table = data.pivot_table(index='primary_mode',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.primary_mode,'y':table['key'],'type':'bar','name':'mode'},3,1)

        fig.update_layout(margin=dict(l=80,r=20,t=50,b=20),showlegend=True,height=800, title_text="Employment characteristics")
        
        return fig      
    
    elif selected_option == 'cut':
        fig = make_subplots(
        rows=3, cols=1,  
        )

        table = data.pivot_table(index='origin',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.origin,'y':table['key'],'type':'bar','name':'origin'},1,1)

        table = data.pivot_table(index='destination',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.destination,'y':table['key'],'type':'bar','name':'destination'},2,1)

        table = data.pivot_table(index='trip_frequency',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.trip_frequency,'y':table['key'],'type':'bar','name':'trip_frequency'},3,1)

        fig.update_layout(showlegend=True,height=850,title_text='Current trip characteristics')
        
        return fig
           

    elif selected_option == 'ftc':
        
        fig = make_subplots(
            rows=3, cols=1,
        )

        table = data.pivot_table(index='commute_most_frequent',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.commute_most_frequent,'y':table['key'],'type':'bar','name':'commute_most_frequent'},1,1)

        table = data.pivot_table(index='com_most_freq',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.com_most_freq,'y':table['key'],'type':'bar','name':'com_most_freq'},2,1)

        table = data.pivot_table(index='mode_most_frequent_commute',values='key',aggfunc='count').reset_index()
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

        table = data.pivot_table(index='satisfaction_trans_options',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.satisfaction_trans_options,'y':table['key'],'type':'bar','name':'satisfaction_trans_options'},1,1)

        table = data.pivot_table(index='satisfaction_safety_of_vehicle',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.satisfaction_safety_of_vehicle,'y':table['key'],'type':'bar','name':'satisfaction_safety_of_vehicle'},1,2)

        table = data.pivot_table(index='satisfaction_safety_of_journey',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.satisfaction_safety_of_journey,'y':table['key'],'type':'bar','name':'satisfaction_safety_of_journey'},2,1)

        table = data.pivot_table(index='quality',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.quality,'y':table['key'],'type':'bar','name':'quality'},2,2)

        table = data.pivot_table(index='waiting_times',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.waiting_times,'y':table['key'],'type':'bar','name':'waiting_times'},3,1)

        table = data.pivot_table(index='location_of_pick_up_and_drop_off',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.location_of_pick_up_and_drop_off,'y':table['key'],'type':'bar','name':'location_of_pick_up_and_drop_off'},3,2)

        table = data.pivot_table(index='fare',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.fare,'y':table['key'],'type':'bar','name':'fare'},4,1)

        table = data.pivot_table(index='comfort_on_the_vehicle',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.comfort_on_the_vehicle,'y':table['key'],'type':'bar','name':'comfort_on_the_vehicle'},4,2)

        fig.update_layout(showlegend=True,height=900,title_text='Passenger satisfaction')
        
        return fig
    elif selected_option == 'pasp':
        
        fig = make_subplots(
        rows=3, cols=1,  
        )

        table = data.pivot_table(index='perception_on_public_transport_likemost',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.perception_on_public_transport_likemost,'y':table['key'],'type':'bar','name':'perception_on_public_transport_likemost'},1,1)

        table = data.pivot_table(index='perception_on_public_transport_likeleast',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.perception_on_public_transport_likeleast,'y':table['key'],'type':'bar','name':'perception_on_public_transport_likeleast'},2,1)

        table = data.pivot_table(index='issues_during_trip',values='key',aggfunc='count').reset_index()
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

        table = data.pivot_table(index='witnessed_crime',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.witnessed_crime,'y':table['key'],'type':'bar','name':'witnessed_crime'},1,1)

        table = data.pivot_table(index='sexual_harasment',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.sexual_harasment,'y':table['key'],'type':'bar','name':'sexual_harasment'},1,2)

        table = data.pivot_table(index='issues_during_trip',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.issues_during_trip,'y':table['key'],'type':'bar','name':'issues_during_trip'},2,1)

        table = data.pivot_table(index='adhering_to_local_covid_regulations',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.adhering_to_local_covid_regulations,'y':table['key'],'type':'bar','name':'adhering_to_local_covid_regulations'},3,1)

        fig.update_layout(showlegend=True,height=900,title_text='Safety and Security')      
        
        return fig
    
    # elif selected_option == 'pay':
            
    #     return fig  
    else:
        fig = make_subplots(
            rows=1, cols=2,
        )
    
        table = data.pivot_table(index='cellphone_payment',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.cellphone_payment,'y':table['key'],'type':'bar','name':'cellphone_payment'},1,1)

        table = data.pivot_table(index='tab_payment',values='key',aggfunc='count').reset_index()
        fig.append_trace({'x':table.tab_payment,'y':table['key'],'type':'bar','name':'tab_payment'},1,2)


        fig.update_layout(showlegend=True,height=400,title_text='Mobile payments')
        
        return fig        
            
        


    # new_df = long_form(dff, selected_option, value) #(input data, selected attribute,value to use in count)

    # trace = go.Bar(x = new_df.index, y=new_df[value],marker_color='lightseagreen')

    # layout = go.Layout( title = selected_option,xaxis={'title':selected_option},yaxis = {'title':'Total'},
    #                     barmode = 'stack', height = 500,margin={'b':0})

    # fig = go.Figure ( data = [trace], layout = layout )
    # fig.update_layout()
    # return fig