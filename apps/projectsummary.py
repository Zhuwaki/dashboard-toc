import pandas
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app


layout = html.Div([ #canvas

    html.Div( # division for content
        [
            dbc.Row( # row for content
                [
                    dbc.Col( # left column on canvas
                        [
                            html.H4('Background'),
                            
                            html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi fermentum massa quis tellus laoreet sollicitudin. Aliquam erat volutpat. Maecenas venenatis vitae elit eget euismod. In rutrum vestibulum orci, ac consequat velit laoreet quis. Praesent vel mauris odio. Donec ipsum diam, eleifend nec tincidunt ac, rutrum nec ex. Maecenas porttitor finibus auctor. Donec nec convallis nisi. Donec eu pulvinar turpis. Fusce ante dui, dignissim sit amet nisi a, gravida pretium massa. Praesent ut enim quis dui faucibus tincidunt vel quis dolor. Etiam fermentum nisi et lacus dignissim lobortis. In hac habitasse platea dictumst. Mauris posuere ipsum lacus, sit amet dictum diam porttitor et. Nam ac magna mollis, dignissim nibh eu, malesuada libero. Cras id urna nec dolor aliquam scelerisque.'),
                            html.P('Quisque semper et eros nec porttitor. Praesent sed ornare erat. Donec tincidunt eu urna in eleifend. Pellentesque risus augue, accumsan non scelerisque at, dictum in lacus. Nam eget bibendum dolor. Aenean egestas augue dui, ac sollicitudin neque sagittis non. Maecenas quis odio eget libero dictum cursus. Sed quis efficitur felis. Duis sed arcu leo. Ut sodales faucibus convallis. Quisque placerat pretium elit, ac volutpat turpis luctus at. Nullam eget aliquam dui. Curabitur tristique metus malesuada, convallis tellus ac, congue mauris. Vivamus rhoncus laoreet diam a tempus. Donec consectetur, ligula vitae tincidunt venenatis, neque ligula ultricies ante, non commodo risus nulla at elit.'),
                            

                        ],xs=12,sm=12,md=12,lg=3,xl=3, className='summary'
                    ), # end of left column on canvas

                    # dbc.Col( # right column on canvas
                    #     [
                    #         html.H4('Methodology'),
                    #         html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi fermentum massa quis tellus laoreet sollicitudin. Aliquam erat volutpat. Maecenas venenatis vitae elit eget euismod. In rutrum vestibulum orci, ac consequat velit laoreet quis. Praesent vel mauris odio. Donec ipsum diam, eleifend nec tincidunt ac, rutrum nec ex. Maecenas porttitor finibus auctor. Donec nec convallis nisi. Donec eu pulvinar turpis. Fusce ante dui, dignissim sit amet nisi a, gravida pretium massa. Praesent ut enim quis dui faucibus tincidunt vel quis dolor. Etiam fermentum nisi et lacus dignissim lobortis. In hac habitasse platea dictumst. Mauris posuere ipsum lacus, sit amet dictum diam porttitor et. Nam ac magna mollis, dignissim nibh eu, malesuada libero. Cras id urna nec dolor aliquam scelerisque.'),
                    #         html.P('Quisque semper et eros nec porttitor. Praesent sed ornare erat. Donec tincidunt eu urna in eleifend. Pellentesque risus augue, accumsan non scelerisque at, dictum in lacus. Nam eget bibendum dolor. Aenean egestas augue dui, ac sollicitudin neque sagittis non. Maecenas quis odio eget libero dictum cursus. Sed quis efficitur felis. Duis sed arcu leo. Ut sodales faucibus convallis. Quisque placerat pretium elit, ac volutpat turpis luctus at. Nullam eget aliquam dui. Curabitur tristique metus malesuada, convallis tellus ac, congue mauris. Vivamus rhoncus laoreet diam a tempus. Donec consectetur, ligula vitae tincidunt venenatis, neque ligula ultricies ante, non commodo risus nulla at elit.'),
                            

                    #     ],width=4,className='summary'

                    # ), # end of left column on canvas
                    dbc.Col( # right column on canvas
                        [
                            #html.H4('Scope'),
                            html.Img(src=app.get_asset_url('method.png'),style={'margin-top':1,'margin-left':0, 'width':'100%'}),
                            #html.Img(src=app.get_asset_url('maseru.png'),style={'margin-top':1,'margin-left':0, 'width':'40%'}),


                        ],xs=12,sm=12,md=12,lg=7,xl=7,className='summary-image'

                    ) # end of left column on canvas
                    
                ]
                
            ) # end of row for content

        ]
    ), # end of division for content
    

    ]) # end of canvas