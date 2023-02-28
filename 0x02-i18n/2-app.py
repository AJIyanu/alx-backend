#!/usr/bin/env python3
"""creates a flask application"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """to configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """set locale en"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> str:
    """route to home"""
    return render_template('0-index.html')


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port)
