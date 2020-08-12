import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from server import flask_app

from app import dash_app
from layouts import layouts
import callbacks

dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@dash_app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dash/':
        return layouts['index']
    else:
        return '404'


if __name__ == '__main__':
    flask_app.run(debug=True)
