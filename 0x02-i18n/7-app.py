#!/usr/bin/env python3
"""creates a flask application"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _


app = Flask(__name__)
babel = Babel(app)


class Config:
    """to configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int) -> dict:
    """fetch user for me"""
    return users.get(user_id, {})


@app.before_request
def before_request() -> None:
    """gets user before handling request"""
    if bool(request.args):
        login_as = int(request.args.get('login_as'))
        user = get_user(login_as)
        g.user = user
    else:
        g.user = {}


@babel.localeselector
def get_locale():
    """set locale en"""
    locale = request.args.get("locale")
    lang = ["en", "fr"]
    loc = g.user
    if loc.get("locale") in lang:
        return loc.get("locale")
    if locale in lang:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """set local time zone"""
    timezone = request.args.get("timezone")
    if timezone is None:
        timezone = g.user.get("timezone")
    if timezone is not None:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            return "UTC"


@app.route("/")
def index() -> str:
    """route to home"""
    home_title = _("home_title")
    home_header = _("home_header")
    username = g.user
    username = username.get("name")
    return render_template('7-index.html',
                           home_title=home_title,
                           home_header=home_header,
                           username=username)


if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = "5000"
    app.run(host=HOST, port=PORT)
