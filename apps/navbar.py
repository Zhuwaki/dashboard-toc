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
        #style={'color':'red'},
    ),
    
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem('Onboard surveys', href = '/apps/onboardProductivity'),
            dbc.DropdownMenuItem('Intercept surveys', href = '/apps/interceptProductivity'),
            dbc.DropdownMenuItem('Rank Count surveys', href = '/apps/rankcountProductivity'),


        ],
        nav=True,
        in_navbar=True,
        label="Productivity",
    ),
        dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem('Intercept summary', href = '/apps/intercept_demo'),
            dbc.DropdownMenuItem('Onboard summary', href = '/apps/onboardData'),
            dbc.DropdownMenuItem('Route demand', href = '/apps/onboardIntervalRoute'),
            dbc.DropdownMenuItem('Vehicle revenue', href = '/apps/onboardIntervalVehicle'),
            dbc.DropdownMenuItem('Route frequency', href = '/apps/routeFrequency'),



        ],
        nav=True,
        in_navbar=True,
        label="Survey summary",
    ),
    
        dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem('Onboard route map', href = '/apps/mapbox'),
            dbc.DropdownMenuItem('Intercept location map', href = '/apps/geoIntercept'),
            #dbc.DropdownMenuItem('Rank Count', href = '/apps/rankcount'),
        ],
        nav=True,
        in_navbar=True,
        label="Geospatial",
        
    )
        ],
    brand = 'Digital Innovation Survey Portal',
    brand_href ='/apps/onboard',
    color='#009999',
    brand_style={'color':'#ffff'},
    #className='nav-bar'
    )
