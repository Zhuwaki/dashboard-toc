import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server
from apps import navbar

from apps import onbaord, interceptDist,rankcount,mapbox,projectsummary,maseruSummary,gaboroneSummary,geoIntercept,onboardDist,intercept_demographic,onboardData,onboardIntervalRoute

app.layout = html.Div([       
    navbar.navbar,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
],style={'height':'100vh'})

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):

    if pathname == '/apps/onboard':
        return onbaord.layout
    elif pathname == '/apps/intercept':
        return onbaord.layout
    elif pathname == '/apps/rankcount':
        return rankcount.layout
    elif pathname == '/apps/projectsummary':
        return projectsummary.layout
    elif pathname == '/apps/maseruSummary':
        return maseruSummary.layout
    elif pathname == '/apps/gaboroneSummary':
        return gaboroneSummary.layout
    elif pathname == '/apps/mapbox':
        return mapbox.layout
    elif pathname == '/apps/geoIntercept':
        return geoIntercept.layout
    elif pathname == '/apps/onboardDist':
        return onboardDist.layout
    elif pathname == '/apps/interceptDist':
        return interceptDist.layout
    elif pathname == '/apps/rankDist':
        return onboardDist.layout
    elif pathname == '/apps/intercept_demo':
        return intercept_demographic.layout
    elif pathname == '/apps/onboardData':
        return onboardData.layout
    elif pathname == '/apps/onboardIntervalRoute':
        return onboardIntervalRoute.layout
    else:
        return projectsummary.layout

if __name__ == '__main__':
    app.run_server(debug=True)