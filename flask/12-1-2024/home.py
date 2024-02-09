from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route("/welcome")
def print_name():
    return "Welcome"
@app.route("/about")
def go():
    return "I am Varshini"
@app.route("/user/<name>")
def print_username(name):
    return name

# @app.route("/contact/<name>")
# def renderHTML(name):
    # return render_template("home.html",name=name)

@app.route("/lists")
def renderHTML():
    names=["varshini","amirtha","preethi","pavithra"]

    return render_template("name.html",list=names)
