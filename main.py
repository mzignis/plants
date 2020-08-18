import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from server import flask_app
import threading
from server.server import server_main_loop

from app import dash_app
from layouts import layouts_
import callbacks

dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@dash_app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dash/':
        return layouts_['index']
    else:
        return layouts_['404']


if __name__ == '__main__':
    # server_thread = threading.Thread(target=server_main_loop)
    # server_thread.start()

    flask_app.run('localhost', debug=True)
