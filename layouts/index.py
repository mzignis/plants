import dash_bootstrap_components as dbc
import dash_html_components as html

from layouts.navbar import navbar


body = html.Div([
    html.H1('Hello World!'),
])


index_layout = html.Div([
    navbar,
    dbc.Container(body, id='index-body'),
])
