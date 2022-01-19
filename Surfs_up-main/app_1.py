# load Dependencies
from flask import Flask
# add instance 'app' to Flask
app = Flask(__name__)
# the root or first route
@app.route("/")
# Create a function called hello_world(). Whenever you make a route in Flask, you put the code you want in that specific route
def hello_world():
    return "<p>Hello, World!</p>"

