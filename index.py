import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server
#from apps import onbaord, intercept,rankcount,app1,geoOnboard

app.layout = html.Div([
    
        html.Div(# division for navigation bar
        [
            dbc.NavbarSimple(
                [
                    dbc.NavItem(dbc.NavLink("Project Summary", href = '/apps/onboard')),
                #    dbc.NavItem(dbc.NavLink("Intercept", href = '/apps/intercept')),
                #    dbc.NavItem(dbc.NavLink("Rank count", href = '/apps/rankcount')),
                   
                    dbc.DropdownMenu(
                       [
                           dbc.DropdownMenuItem('Maseru', href = '/apps/onboard'),
                           dbc.DropdownMenuItem('Gaborone', href = '/apps/intercept'),
                       ],
                       nav=True,
                       in_navbar=True,
                       label="City Summary",
                   ),
                   
                   dbc.DropdownMenu(
                       [
                           dbc.DropdownMenuItem('Onbaord', href = '/apps/onboard'),
                           dbc.DropdownMenuItem('Intercept', href = '/apps/intercept'),
                           dbc.DropdownMenuItem('Rank Count', href = '/apps/rankcount'),

                       ],
                       nav=True,
                       in_navbar=True,
                       label="Survey Summary",
                   ),
                    dbc.DropdownMenu(
                       [
                           dbc.DropdownMenuItem('Onbaord', href = '/apps/geoOnboard'),
                           dbc.DropdownMenuItem('Intercept', href = '/apps/intercept'),
                           dbc.DropdownMenuItem('Rank Count', href = '/apps/rankcount'),

                       ],
                       nav=True,
                       in_navbar=True,
                       label="Geospatial Summary",
                   )
                    ],
                brand = 'Field summary reports',
                brand_href ='/apps/onboard'
                )
            ]
        ),
    
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/onboard':
        return onbaord.layout
    elif pathname == '/apps/intercept':
        return intercept.layout
    elif pathname == '/apps/rankcount':
        return rankcount.layout
    elif pathname == '/apps/geoOnboard':
        return geoOnboard.layout
    else:
        return 'Page not found'

if __name__ == '__main__':
    app.run_server(debug=True)