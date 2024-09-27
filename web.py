from flask import Flask, send_from_directory
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
env = Environment(loader=FileSystemLoader("www"))

@app.route("/")
def index():
    t = env.get_template("index.html")
    return t.render()

@app.route('/<path:path>')
def send_report(path):
    response = send_from_directory("www", path, as_attachment=True)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate" # убрать для продакта!!!
    return response