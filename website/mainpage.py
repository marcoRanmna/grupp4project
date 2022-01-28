from flask import Blueprint, render_template

main_page = Blueprint("main", __name__)


@main_page.route("/main-page")
def main():
    return render_template("main.html")
