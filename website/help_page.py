from flask import Blueprint, render_template

help_page1 = Blueprint("help1", __name__)


@help_page1.route("/help-page", methods=["GET", "POST"])
def help():
    return render_template("help.html")
