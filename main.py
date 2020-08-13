import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from server import flask_app
import threading
from server.server import server_main_loop

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
    server_thread = threading.Thread(target=server_main_loop)
    server_thread.start()

    flask_app.run('192.168.0.100', debug=True)

    # import sqlite3
    # import pandas as pd
    #
    # conn = sqlite3.connect('plants.db')
    # q_result = pd.read_sql_query('select soil_humidity from soil_humidity order by datetime desc limit 1', conn)
    # if q_result.empty:
    #     print('--.-- %')
    #
    # soil_humidity = q_result.values[0][0]
    # print(soil_humidity)