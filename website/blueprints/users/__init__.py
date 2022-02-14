import json

from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.controllers.user_controller import add_data, account_settings, get_user_data, password_settings, get_data_for_user_by_date, add_diary_note, get_all_diary_notes_for_user
from flask_login import login_required, logout_user, current_user


bp_users = Blueprint("bp_users", __name__)


@bp_users.before_request
def before_request():
    if not current_user.is_authenticated:
        return redirect(url_for('views.home'))


@bp_users.route("/logout", methods=["GET"])
def logout_get():
    return render_template("signout.html")


@bp_users.route("/logout", methods=["POST"])
def logout_post():
    logout_user()
    return redirect(url_for("main.main"))


@bp_users.route("/add-data", methods=["GET"])
def add_data_get():
    return render_template("adddata.html")


@bp_users.route("/add-data", methods=["POST"])
def add_data_post():
    date = request.form.get("date")
    steps = request.form.get("steps")
    weight = request.form.get("weight")
    calories_eaten = request.form.get("caloriesEaten")
    calories_burned = request.form.get("caloriesBurned")
    average_pulse = request.form.get("averagePulse")

    add_data(date, steps, weight, calories_eaten, calories_burned, average_pulse)
    flash("Data added.", category="success")
    return redirect(url_for("bp_users.add_data_post"))


@bp_users.route("/account-settings", methods=["GET"])
def account_settings_get():
    user_data = get_user_data()
    return render_template("accountsettings.html", user_data=user_data)


@bp_users.route("/account-settings", methods=["POST"])
def account_settings_post():
    first_name = request.form.get("firstName")
    last_name = request.form.get("lastName")
    email = request.form.get("email")
    bio = request.form.get("bio")
    old_password = request.form.get("oldPassword1")
    new_password = request.form.get("newPassword1")
    if old_password != "":
        if not password_settings(old_password, new_password):
            flash("You typed in the wrong old password")
            return redirect(url_for("bp_users.account_settings_get"))
        flash("Password updated")
        flash("Login again to confirm your changes")
        return redirect(url_for("main.main"))
    elif email == "":
        flash("You can't leave boxes empty")
        return redirect(url_for("bp_users.account_settings_get"))
    account_settings(first_name, last_name, email, bio)
    flash("Account settings updated", category="success")
    flash("Login again to confirm your changes")
    return redirect(url_for("main.main"))


@bp_users.route("/calendar", methods=["GET"])
def calendar_get():
    return render_template("calendar.html")


@bp_users.route("/calendar", methods=["POST"])
def calendar_post():
    date = request.form.get("date")
    data_user = get_data_for_user_by_date(date)
    print(data_user)
    if not data_user:
        flash("No data for that day")
    return render_template("calendar.html", data_user=data_user)


@bp_users.route("/0186510e7b7767cc957fe1a77da0977fca7577e3b491681a587cbe348d390919", methods=["GET"])
def user_data_get():
    user_data = get_user_data()
    user_data = user_data.__dict__
    user_data["_id"] = str(user_data["_id"])
    del user_data["date_created"]
    del user_data["last_signin"]
    print(user_data)

    return json.dumps(user_data)


@bp_users.route("/diary", methods=["POST"])
def diary():
    diary_entry = request.form.get("diary_entry")
    add_diary_note(diary_entry)
    flash("Your diary note has been added!.", category="success")
    return redirect(request.referrer)
    # return render_template("diary.html", diary_entry=diary_entry)


@bp_users.route("/diary", methods=["GET"])
def diary_get():
    diary_entries = get_all_diary_notes_for_user()
    return render_template("diary.html", diary_entries=diary_entries)
