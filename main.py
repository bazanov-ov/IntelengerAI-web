import config
from flask import Flask, render_template, json, redirect, url_for


app = Flask(__name__)


from endpoints.accounts import *





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4431)