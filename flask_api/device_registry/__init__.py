from . import conway_suite
from flask import Flask
app=Flask(__name__)

@app.route("/alive",methods=['GET'])
def hello():
    return "Hello World"

@app.route("/api/v1/conway/<int:num>",methods=['GET'])
def index(num):
    return conway_suite.get_sequence(num)

@app.errorhandler(404)
def errorpage(error):
    return "Error in the path"

