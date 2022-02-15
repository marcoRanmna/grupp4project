from website.controllers.user_controller import add_data, account_settings, get_user_data, password_settings, \
    get_data_for_user_by_date, add_diary_note, get_all_diary_notes_for_user, weight_progress, add_training, add_sleep, \
    get_sleep_for_user_by_date, get_training_for_user_by_date, get_data_for_user, get_sleep_data_by_id, \
    get_training_data_by_id
from flask import Blueprint, render_template, request, redirect, url_for, flash, Flask
from flask_login import logout_user, current_user

app = Flask(__name__)
bp_users = Blueprint("bp_users", __name__)


@bp_users.before_request
def before_request():
    if not current_user.is_authenticated:
        return redirect(url_for('main.main'))


@bp_users.route("/logout", methods=["GET"])
def logout_get():
    return render_template("signout.html")


@bp_users.route("/logout", methods=["POST"])
def logout_post():
    logout_user()
    return redirect(url_for("bp_open.main"))


@bp_users.route("/add-data", methods=["GET"])
def add_data_get():
    user = get_user_data()
    return render_template("adddata.html", user=user)


@bp_users.route("/add-data", methods=["POST"])
def add_data_post():
    daily_date = request.form.get("date")
    steps = request.form.get("steps")
    training_time = request.form.get("trainingTime")
    weight = request.form.get("weight")
    calories_eaten = request.form.get("caloriesEaten")
    calories_burned = request.form.get("caloriesBurned")
    average_pulse = request.form.get("averagePulse")
    highest_pulse = request.form.get("highestPulse")
    lowest_pulse = request.form.get("lowestPulse")
    average_stress = request.form.get("averageStress")
    average_o2 = request.form.get("averageO2")
    goal_weight = request.form.get("weightGoal")
    start_weight = request.form.get("startWeight")
    current_weight = request.form.get("currentWeight")
    calorie_goal = request.form.get("calorieGoal")
    training_date = request.form.get("trainingDate")
    training_form = request.form.get("trainingSession")
    training_pulse = request.form.get("trainingPulse")
    duration = request.form.get("duration")
    sleep_date = request.form.get("sleepDate")
    total_sleep = request.form.get("totalSleep")
    deep_sleep = request.form.get("deepSleep")
    light_sleep = request.form.get("lightSleep")

    if daily_date:
        add_data(daily_date, steps, training_time, weight, calories_eaten, calories_burned, average_pulse, highest_pulse, lowest_pulse, average_stress, average_o2)
        flash("Data added.", category="success")
        return redirect(url_for("bp_users.add_data_post"))
    if training_date:
        add_training(training_date, training_form, training_pulse, duration)
        flash("Training session added.")
        return redirect(url_for("bp_users.add_data_post"))
    if sleep_date:
        add_sleep(sleep_date, total_sleep, deep_sleep, light_sleep)
        flash("Sleep added.")
        return redirect(url_for("bp_users.add_data_post"))
    if current_weight:
        weight_progress(goal_weight, start_weight, current_weight, calorie_goal)
        flash("Weight progress updated.", category="success")
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
        return redirect(url_for("bp_open.main"))
    elif email == "":
        flash("You can't leave boxes empty")
        return redirect(url_for("bp_users.account_settings_get"))
    account_settings(first_name, last_name, email, bio)
    flash("Account settings updated", category="success")
    flash("Login again to confirm your changes")
    return redirect(url_for("bp_open.main"))


@bp_users.route("/calendar", methods=["GET"])
def calendar_get():
    return render_template("calendar.html")


@bp_users.route("/calendar", methods=["POST"])
def calendar_post():
    date = request.form.get("date")
    data_user = get_data_for_user_by_date(date)
    training_user = get_training_for_user_by_date(date)
    sleep_user = get_sleep_for_user_by_date(date)
    # if not data_user:
    #     flash("No data for that day")
    return render_template("calendar.html", data_user=data_user, training_user=training_user, sleep_user=sleep_user)


@bp_users.route("/diary", methods=["POST"])
def diary():
    diary_entry = request.form.get("diary_entry")
    add_diary_note(diary_entry)
    flash("Your diary note has been added!.", category="success")
    return redirect(request.referrer)


@bp_users.route("/diary", methods=["GET"])
def diary_get():
    diary_entries = get_all_diary_notes_for_user()
    return render_template("diary.html", diary_entries=diary_entries)


@bp_users.route("/", methods=["GET"])
def home():
    user_data = get_data_for_user()
    user = get_user_data()
    sleep = get_sleep_data_by_id()
    training = get_training_data_by_id()
    date = []
    pulse = []
    stress = []
    o2 = []

    for data in user_data:
        date.append(data.date)
        pulse.append(data.average_pulse)
        stress.append(data.average_stress)
        o2.append(data.average_o2)

    return render_template("home.html", date=date, pulse=pulse, stress=stress, o2=o2, user=user, sleep=sleep, training=training)


@bp_users.route("/help-page", methods=["GET"])
def help():
    return render_template("help.html")


@bp_users.route("/profile-preference", methods=["GET"])
def profile_preference():
    return render_template("profilepreference.html")


@bp_users.route("/synchronize-page", methods=["GET"])
def synchronize():
    return render_template("synchronize.html")
