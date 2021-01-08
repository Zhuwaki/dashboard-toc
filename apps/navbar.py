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
            dbc.DropdownMenuItem('Intercept', href = '/apps/intercept_demo'),
            dbc.DropdownMenuItem('Onboard', href = '/apps/onboardData'),
            dbc.DropdownMenuItem('Onboard Interval Route', href = '/apps/onboardIntervalRoute'),
            # dbc.DropdownMenuItem('Rank Count', href = '/apps/rankcount'),


        ],
        nav=True,
        in_navbar=True,
        label="Survey summary",
    ),
    
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem('Onboard distributions', href = '/apps/onboardDist'),
            dbc.DropdownMenuItem('Intercept distributions', href = '/apps/interceptDist'),
            dbc.DropdownMenuItem('Rank distributions', href = '/apps/rankDist'),
        ],
        nav=True,
        in_navbar=True,
        label="Distributions",
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
    brand = 'TOC Dashboard',
    brand_href ='/apps/onboard',
    color='#009999',
    brand_style={'color':'#ffff'},
    className='nav-bar'
    )
