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