import dash_bootstrap_components as dbc
import dash_html_components as html


def create_card(name):
    card_content = [
        dbc.CardHeader(name),
        dbc.CardBody(
            [
                html.H6("{} soil humidity".format(name), className="card-title"),
                html.H1(
                    "99.98 %",
                    className="card-text",
                ),
                dbc.Button(
                    "Watered!", color="success", className="mt-auto"
                ),
            ]
        ),
    ]

    return card_content

card1 = dbc.Card([
        dbc.CardHeader('Plant1'),
        dbc.CardBody(
            [
                html.H6("Plant1 soil humidity", className="card-title"),
                html.H1("99.98 %", id='card1-humi-value', className="card-text",),
                dbc.Button("Watered!", id='card1-button', color="success", className="mt-auto"),
            ]
        ),
    ],
    id='plant1-card',
    color="success",
    outline=True)

card2 = dbc.Card([
        dbc.CardHeader('Plant2'),
        dbc.CardBody(
            [
                html.H6("Plant2 soil humidity", className="card-title"),
                html.H1("99.98 %", id='card2-humi-value', className="card-text",),
                dbc.Button("Watered!", id='card2-button', color="success", className="mt-auto"),
            ]
        ),
    ],
    id='plant2-card',
    color="success",
    outline=True)


card3 = dbc.Card([
        dbc.CardHeader('Plant3'),
        dbc.CardBody(
            [
                html.H6("Plant3 soil humidity", className="card-title"),
                html.H1("99.98 %", id='card3-humi-value', className="card-text",),
                dbc.Button("Watered!", id='card3-button', color="success", className="mt-auto"),
            ]
        ),
    ],
    id='plant3-card',
    color="success",
    outline=True)


card4 = dbc.Card([
        dbc.CardHeader('Plant4'),
        dbc.CardBody(
            [
                html.H6("Plant4 soil humidity", className="card-title"),
                html.H1("99.98 %", id='card4-humi-value', className="card-text",),
                dbc.Button("Watered!", id='card4-button', color="success", className="mt-auto"),
            ]
        ),
    ],
    id='plant4-card',
    color="success",
    outline=True)