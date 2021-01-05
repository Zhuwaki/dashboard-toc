import dash_bootstrap_components as dbc
import dash_html_components as html

navbar =  dbc.NavbarSimple(
    
    [
        dbc.NavItem(dbc.NavLink("Project Summary", href = '/apps/projectsummary')),
    #    dbc.NavItem(dbc.NavLink("Intercept", href = '/apps/intercept')),
    #    dbc.NavItem(dbc.NavLink("Rank count", href = '/apps/rankcount')),
    
        dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem('Maseru', href = '/apps/maseru'),
            dbc.DropdownMenuItem('Gaborone', href = '/apps/gaborone'),
        ],
        nav=True,
        in_navbar=True,
        label="City Summary",
    ),
    
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem('Onboard', href = '/apps/onboard'),
            dbc.DropdownMenuItem('Intercept', href = '/apps/intercept'),
            dbc.DropdownMenuItem('Rank Count', href = '/apps/rankcount'),


        ],
        nav=True,
        in_navbar=True,
        label="Productivity Summary",
    ),
    dbc.DropdownMenu(
        [
            # dbc.DropdownMenuItem('Onboard', href = '/apps/onboard'),
            # dbc.DropdownMenuItem('Intercept', href = '/apps/intercept'),
            # dbc.DropdownMenuItem('Rank Count', href = '/apps/rankcount'),
            dbc.DropdownMenuItem('Onboard', href = '/apps/onboardDist'),

        ],
        nav=True,
        in_navbar=True,
        label="Survey Summary",
    ),
        dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem('Onbaord', href = '/apps/mapbox'),
            dbc.DropdownMenuItem('Intercept', href = '/apps/geoIntercept'),
            #dbc.DropdownMenuItem('Rank Count', href = '/apps/rankcount'),

        ],
        nav=True,
        in_navbar=True,
        label="Geospatial Summary",
        
    )
        ],
    brand = 'Digital Innovation Dashboard',
    brand_href ='/apps/onboard',
    color='#009999',
    brand_style={'color':'#ffff'},
    sticky='sticky'
    )
