from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

from flask import current_app

@main.route("/data")
def get_data():
    data = list(current_app.mongo_db.collection_name.find())
    # process data or return as JSON
    return {"data": data}
