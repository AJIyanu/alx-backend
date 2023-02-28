#!/usr/bin/env python3
"""creates a flask application"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index() -> str:
    """route to home"""
    return render_template('0-index.html')


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port)
