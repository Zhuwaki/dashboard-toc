import dash_bootstrap_components as dbc
import dash_html_components as html

navbar =  dbc.NavbarSimple(
    
    [
        #dbc.NavItem(dbc.NavLink("Project Summary", href = '/apps/projectsummary')),
    
        dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem('Project summary', href = '/apps/projectSummary'),
            dbc.DropdownMenuItem('Maseru', href = '/apps/maseruSummary'),
            dbc.DropdownMenuItem('Gaborone', href = '/apps/gaboroneSummary'),
        ],
        nav=True,
        in_navbar=True,
        label="About",
    ),
    
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem('Onboard', href = '/apps/onboard'),
            dbc.DropdownMenuItem('Intercept', href = '/apps/intercept'),
            dbc.DropdownMenuItem('Rank Count', href = '/apps/rankcount'),


        ],
        nav=True,
        in_navbar=True,
        label="Productivity",
    ),
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem('Onboard', href = '/apps/onboardDist'),
            dbc.DropdownMenuItem('Intercept', href = '/apps/interceptDist'),
            dbc.DropdownMenuItem('Rank', href = '/apps/rankDist'),
        ],
        nav=True,
        in_navbar=True,
        label="Survey",
    ),
        dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem('Onbaord', href = '/apps/mapbox'),
            dbc.DropdownMenuItem('Intercept', href = '/apps/geoIntercept'),
            #dbc.DropdownMenuItem('Rank Count', href = '/apps/rankcount'),
        ],
        nav=True,
        in_navbar=True,
        label="Geospatial",
        
    )
        ],
    brand = 'TOC',
    brand_href ='/apps/onboard',
    color='#009999',
    brand_style={'color':'#ffff'},
    className='nav-bar'
    )
