#!/usr/bin/env python3
"""Setup a basic Flask app and instantiate the Babel object in the app. Store
it in a module-level variable named babel"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class for babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def home():
    """Function for home page"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
