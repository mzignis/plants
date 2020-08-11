import dash_bootstrap_components as dbc
import dash_html_components as html

from layouts.navbar import navbar
from layouts.plant_widget import create_card




body = html.Div([
    html.Br(),
    dbc.CardDeck([
        dbc.Col(dbc.Card(create_card('Plant 1'), color="success", outline=True)),
        dbc.Col(dbc.Card(create_card('Plant 2'), color="success", outline=True)),
        dbc.Col(dbc.Card(create_card('Plant 3'), color="success", outline=True)),
        dbc.Col(dbc.Card(create_card('Plant 4'), color="success", outline=True)),
    ]),
])


index_layout = html.Div([
    navbar,
    dbc.Container(body, id='index-body'),
])
