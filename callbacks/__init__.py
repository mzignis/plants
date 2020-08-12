from app import dash_app
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc

from server.client import MyClient




@dash_app.callback(Output("card1-humi-value", "children"),
                   [Input("index-timer", "n_intervals")])
def timeout_callback(args):
    print('reading humidity:', args)
    client = MyClient('mac')
    adc = client.read_humidity()

    return '{0:.2f} %'.format(adc)


@dash_app.callback([Output("card1-button", "children"), Output("card1-interval", "disabled")],
                   [Input("card1-button", "n_clicks"), Input("card1-interval", "n_intervals")],
                   [State("card1-button", "children")])
def on_button_clicked(n_clicks, n_intervals, children):
    print(n_clicks, n_intervals, children)
    client = MyClient('mac')
    if not n_clicks:
        client.stop_watering()
        return 'Watered!', True

    if children == 'Watered!':
        client.start_watering()
        return [dbc.Spinner(size="sm"), " Watering..."], False
    else:
        client.stop_watering()
        return 'Watered!', True
