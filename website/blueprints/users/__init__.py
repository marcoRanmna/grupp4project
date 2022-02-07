from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.controllers.user_controller import add_data, account_settings

bp_users = Blueprint("bp_users", __name__)


@bp_users.route("/logout")
def logout():
    return "<p>Logout</p>"


@bp_users.route("/add-data", methods=["GET"])
def add_data_get():
    return render_template("adddata.html")


@bp_users.route("/add-data", methods=["POST"])
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


@bp_users.route("/account-settings", methods=["GET"])
def account_settings_get():
    return render_template("accountsettings.html")


@bp_users.route("/account-settings", methods=["POST"])
def account_settings_post():
    first_name = request.form.get("firstName")
    last_name = request.form.get("lastName")
    email = request.form.get("email")
    bio = request.form.get("bio")
    account_settings(first_name, last_name, email, bio)
    flash("Account settings updated", category="success")
    return redirect(url_for("bp_users.account_settings_get"))


