from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.controllers.user_controller import add_data

bp_users = Blueprint("bp_users", __name__)


@bp_users.route("/logout")
def logout():
    return "<p>Logout</p>"


@bp_users.route("/add-data", methods=["GET", "POST"])
def add_data():
    return render_template("adddata.html")


@bp_users.route("/add-data", methods=["GET", "POST"])
def add_data_post():
    if request.method == "POST":
        date = request.form.get("date")
        steps = request.form.get("steps")
        weight = request.form.get("weight")
        calories_eaten = request.form.get("caloriesEaten")
        calories_burned = request.form.get("caloriesBurned")
        average_pulse = request.form.get("averagePulse")

        add_data(date, steps, weight, calories_eaten, calories_burned, average_pulse)
        flash("Data added.", category="success")
        return redirect(url_for("bp_open.login"))


