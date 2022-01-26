from flask import Blueprint, render_template

synchronize_page = Blueprint("synchronize", __name__)


@synchronize_page.route("/synchronize-page", methods=["GET", "POST"])
def synchronize():
    return render_template("synchronize.html")
