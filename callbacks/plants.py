import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

from app import dash_app
from server.client import MyClient


@dash_app.callback([Output("card1-button", "children"), Output("card1-button", "color"), Output("card1", 'color'),
                    Output("card1-button", "disabled"), Output("card1-interval", "disabled")],
                   [Input("card1-button", "n_clicks"), Input("card1-interval", "n_intervals")],
                   [State("card1-button", "children")])
def on_plant1_button_clicked(n_clicks, n_intervals, children):
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


@dash_app.callback([Output("card2-button", "children"), Output("card2-button", "color"), Output("card2", 'color'),
                    Output("card2-button", "disabled"), Output("card2-interval", "disabled")],
                   [Input("card2-button", "n_clicks"), Input("card2-interval", "n_intervals")],
                   [State("card2-button", "children")])
def on_plant2_button_clicked(n_clicks, n_intervals, children):
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


@dash_app.callback([Output("card3-button", "children"), Output("card3-button", "color"), Output("card3", 'color'),
                    Output("card3-button", "disabled"), Output("card3-interval", "disabled")],
                   [Input("card3-button", "n_clicks"), Input("card3-interval", "n_intervals")],
                   [State("card3-button", "children")])
def on_plant3_button_clicked(n_clicks, n_intervals, children):
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


@dash_app.callback([Output("card4-button", "children"), Output("card4-button", "color"), Output("card4", 'color'),
                    Output("card4-button", "disabled"), Output("card4-interval", "disabled")],
                   [Input("card4-button", "n_clicks"), Input("card4-interval", "n_intervals")],
                   [State("card4-button", "children")])
def on_plant4_button_clicked(n_clicks, n_intervals, children):
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