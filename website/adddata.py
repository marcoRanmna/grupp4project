from flask import Blueprint, render_template

add_data = Blueprint("adddata", __name__)


@add_data.route("/add-data", methods=["GET", "POST"])
def adddata():
    return render_template("adddata.html")
