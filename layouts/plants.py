import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import dash_table
import pandas as pd
import sqlite3

from layouts.navbar import navbar


def read_watering_table(plant_id):
    conn = sqlite3.connect('plants.db')
    query = 'select type, soil_humidity, datetime from watering ' \
            'where plant_id == {} ' \
            'order by datetime desc ' \
            'limit 10'.format(plant_id)
    df = pd.read_sql_query(query, conn).drop_duplicates(subset=['datetime']).reset_index(drop=True)
    return df



desc = 'faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam malesuada bibendum arcu ' \
       'vitae elementum curabitur vitae nunc sed velit dignissim sodales ut eu sem integer vitae justo eget magna ' \
       'fermentum iaculis eu non diam phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet enim ' \
       'tortor at auctor urna nunc'

dropdown_options = ['Soil humidity (ADC)', 'Air temperature', 'Air pressure',
                    'Air humidity', 'Rain (ADC)', 'Light (ADC)']

body = dbc.Container([
    html.Br(),
    html.H1('Plant1'),
    html.Br(),
    html.H6(desc),
    html.Br(),

    html.Hr(),
    html.H3('Data history'),
    html.Br(),
    dcc.Dropdown(
        id='plant1-dropdown',
        options=[{'label': label, 'value': label} for label in dropdown_options],
        value=dropdown_options[0],
    ),
    dcc.Graph(id='plant1-graph'),
    html.Br(),

    html.Hr(),
    html.H3('Watering history'),
    html.Br(),
    dash_table.DataTable(
        id='plant1-table',
        columns=[{"name": i, "id": i} for i in read_watering_table(1).columns],
        data=read_watering_table(1).to_dict('records'),
    ),

    html.Br(),
    html.Br(),

])


plant1_page = html.Div([
    navbar,
    body,
])

