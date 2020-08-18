import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from layouts.navbar import navbar
from layouts.plant_widget import card1, card2, card3, card4



body = html.Div([

    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Img(src='https://cdn3.iconfinder.com/data/icons/weather-610/64/weather_sun_sunny_cloud-256.png',
                     height=125, id='index-weather-icon'),
            html.Br(),

            html.H5('Temperature'),
            html.H1('23.3 °C', id='index-temperature'),
            html.Hr(),

            html.H6('Pressure'),
            html.H3('1223.3 hPa', id='index-pressure'),
            html.Hr(),

            html.H6('Humidity'),
            html.H3('23.3 %', id='index-humidity'),

        ], width=2),

        dbc.Col([
            card1,
            html.Br(),
            card3
        ]),

        dbc.Col([
            card2,
            html.Br(),
            card4
        ]),
    ]),
])


index_layout = html.Div([
    navbar,
    dbc.Container(body, id='index-body'),

    dcc.Interval(id='index-timer', interval=30000),
    html.Div([], id='index-placeholder')
])
