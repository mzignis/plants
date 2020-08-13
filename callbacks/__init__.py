from app import dash_app
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
import sqlite3

from server.client import MyClient


@dash_app.callback(Output("card1-humi-value", "children"),
                   [Input("index-timer", "n_intervals")])
def timeout_callback(args):
    print('reading humidity:', args)
    conn = sqlite3.connect('plants.db')
    q_result = pd.read_sql_query('select soil_humidity from soil_humidity order by datetime desc limit 1', conn)
    if q_result.empty:
        return '--.-- %'
    soil_humidity = q_result.values[0][0]
    return soil_humidity


@dash_app.callback([Output("card1-button", "children"), Output("card1-button", "color"), Output("card1", 'color'),
                    Output("card1-button", "disabled"), Output("card1-interval", "disabled")],
                   [Input("card1-button", "n_clicks"), Input("card1-interval", "n_intervals")],
                   [State("card1-button", "children")])
def on_button_clicked(n_clicks, n_intervals, children):
    print(n_clicks, n_intervals, children)
    client = MyClient('mac')
    if not n_clicks:
        client.stop_watering()
        return 'Watered!', 'success', 'success', False, True

    if children == 'Watered!':
        client.start_watering()
        return [dbc.Spinner(size="sm"), " Watering..."], 'primary', 'primary', True, False
    else:
        client.stop_watering()
        return 'Watered!', 'success', 'success', False, True
