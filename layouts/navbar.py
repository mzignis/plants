import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Plant 1", href="/dash/plant1"),
            dbc.DropdownMenuItem("Plant 2", href="#"),
            dbc.DropdownMenuItem("Plant 3", href="#"),
            dbc.DropdownMenuItem("Plant 4", href="#"),
        ],
        nav=True,
        in_navbar=True,
        label="Plants",
    ),
    brand="PlantsApp",
    brand_href="/dash/",
    sticky="top",
    color="dark",
    dark=True,
)