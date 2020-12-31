import dash_bootstrap_components as dbc
import dash_html_components as html

navbar =  dbc.NavbarSimple(
    
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
