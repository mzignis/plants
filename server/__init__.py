from flask import Flask, redirect


flask_app = Flask(__name__)


@flask_app.route('/')
@flask_app.route('/index')
@flask_app.route('/home')
def render_dashboard():
    return redirect('/dash')


if __name__ == '__main__':
    pass
