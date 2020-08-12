import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from layouts.navbar import navbar
from layouts.plant_widget import card1, card2, card3, card4




body = html.Div([
    html.Br(),
    dbc.CardDeck([card1, card2, card3, card4]),
])


index_layout = html.Div([
    navbar,
    dbc.Container(body, id='index-body'),

    dcc.Interval(id='index-timer', interval=15000),
    html.Div([], id='index-placeholder')
])
