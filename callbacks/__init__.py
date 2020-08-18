from app import dash_app
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
import sqlite3
from tools import relative_pressure

from server.client import MyClient


@dash_app.callback([Output("card1-humi-value", "children"), Output('index-temperature', 'children'),
                    Output('index-pressure', 'children'), Output('index-humidity', 'children')],
                   [Input("index-timer", "n_intervals")])
def index_timer_callback(args):
    print('reading humidity:', args)
    conn = sqlite3.connect('plants.db')
    soil_humidity = pd.read_sql_query('select soil_humidity from soil_humidity order by datetime desc limit 1', conn)
    temperature = pd.read_sql_query('select air_temperature from soil_humidity order by datetime desc limit 1', conn)
    pressure = pd.read_sql_query('select air_pressure from soil_humidity order by datetime desc limit 1', conn)
    humidity = pd.read_sql_query('select air_humidity from soil_humidity order by datetime desc limit 1', conn)

    pressure = '{0:.2f} hPa'.format(relative_pressure(float(pressure.values[0][0]) / 100.,
                                                      float(temperature.values[0][0]),
                                                      288))
    temperature = '{0:.2f} °C'.format(float(temperature.values[0][0]))
    humidity = '{0:.2f} %'.format(float(humidity.values[0][0]))
    print(temperature, pressure, humidity)

    if soil_humidity.empty:
        return '--.-- %', temperature, pressure, humidity
    soil_humidity = soil_humidity.values[0][0]

    if soil_humidity is None:
        return '--.-- %', temperature, pressure, humidity

    return soil_humidity, temperature, pressure, humidity


@dash_app.callback([Output("card1-button", "children"), Output("card1-button", "color"), Output("card1", 'color'),
                    Output("card1-button", "disabled"), Output("card1-interval", "disabled")],
                   [Input("card1-button", "n_clicks"), Input("card1-interval", "n_intervals")],
                   [State("card1-button", "children")])
def on_button_clicked(n_clicks, n_intervals, children):
    print(n_clicks, n_intervals, children)
    client = MyClient('mac')
    if not n_clicks:
        # client.stop_watering()
        return 'Watered!', 'success', 'success', False, True

    if children == 'Watered!':
        # client.start_watering()
        return [dbc.Spinner(size="sm"), " Watering..."], 'primary', 'primary', True, False
    else:
        # client.stop_watering()
        return 'Watered!', 'success', 'success', False, True
