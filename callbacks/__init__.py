import sqlite3

import pandas as pd
import plotly.express as px
from dash.dependencies import Output, Input

import callbacks.plants
from app import dash_app
from layouts.plants import dropdown_options
from tools import relative_pressure


table_columns = ['adc_value', 'air_temperature', 'air_pressure', 'air_humidity', 'rain', 'light']
values_dict = dict(zip(dropdown_options, table_columns))


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


@dash_app.callback(Output('plant1-graph', 'figure'),
                   [Input('plant1-dropdown', 'value')])
def on_plant1_drop_down(args):
    value = values_dict[args]

    conn = sqlite3.connect('plants.db')
    query = 'select datetime, {} from soil_humidity ' \
            'where plant_id == 1 ' \
            'order by datetime desc ' \
            'limit 100'.format(value)
    df = pd.read_sql_query(query, conn).drop_duplicates(subset=['datetime']).reset_index(drop=True)
    fig = px.line(x=df['datetime'], y=df['{}'.format(value)].astype(float), line_shape='spline')

    return fig





if __name__ == '__main__':
    pass
