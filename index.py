import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from navbar import navbar
from app import server
from apps import onbaord, intercept,rankcount,mapbox,projectsummary,maseru,gaborone,geoIntercept,onboardDist

app.layout = html.Div([       
    navbar,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
],style={'height':'100vh'})

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):

    if pathname == '/apps/onboard':
        return onbaord.layout
    elif pathname == '/apps/intercept':
        return intercept.layout
    elif pathname == '/apps/rankcount':
        return rankcount.layout
    elif pathname == '/apps/projectsummary':
        return projectsummary.layout
    elif pathname == '/apps/maseru':
        return maseru.layout
    elif pathname == '/apps/gaborone':
        return gaborone.layout
    elif pathname == '/apps/mapbox':
        return mapbox.layout
    elif pathname == '/apps/geoIntercept':
        return geoIntercept.layout
    
    elif pathname == '/apps/onboardDist':
        return onboardDist.layout
    else:
        return projectsummary.layout

if __name__ == '__main__':
    app.run_server(debug=True)