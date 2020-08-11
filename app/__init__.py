import dash_bootstrap_components as dbc
from dash import Dash

from server import flask_app


dash_app = Dash(__name__,
                server=flask_app,
                url_base_pathname='/dash/',
                external_stylesheets=[dbc.themes.BOOTSTRAP])
