from app import dash_app
from dash.dependencies import Output, Input
import paho.mqtt.client as mqtt
import dash_html_components as html
import time

from server.client import MyClient


SERVER_IP = '192.168.0.101'


@dash_app.callback(Output("card1-humi-value", "children"),
                   [Input("index-timer", "n_intervals")])
def timeout_callback(args):

    client = MyClient('mac')
    adc = client.main()
    print(adc)

    return adc
