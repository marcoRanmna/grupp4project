import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user
from website.controllers.user_controller import create_user, signin_user

bp_open = Blueprint("bp_open", __name__)


@bp_open.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@bp_open.get("/sign-up")
def signup_get():
    return render_template("sign_up.html")


@bp_open.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
            return render_template("sign_up.html")
        elif len(first_name) < 2:
            flash("first name must be greater than 1 character.", category="error")
            return render_template("sign_up.html")
        elif len(last_name) < 2:
            flash("first name must be greater than 1 character.", category="error")
            return render_template("sign_up.html")
        elif password1 != password2:
            flash("Passwords don't match.", category="error")
            return render_template("sign_up.html")
        elif len(password1) < 7:
            flash("Password must be att at least 7 characters.", category="error")
            return render_template("sign_up.html")
        else:
            flash("Account was created.", category="success")
            create_user(first_name, last_name, email, password1)
            return redirect(url_for("bp_open.login"))


@bp_open.get('/login')
def signin_get():
    return render_template('login.html')


@bp_open.post('/login')
def signin_post():
    email = request.form.get('email')
    signin_user(email)
    # password = request.form.get('password')
    # from website.persistence.models import User
    # user = User.find(email=email).first_or_none()
    # if user is None:
    #     flash('Error signing in. Check your email and password!')
    #     return redirect(url_for('bp_open.signin_get'))
    #
    # elif password != user.password:
    #     flash('Error signing in. Check your email and password!')
    #     return redirect(url_for('bp_open.signin_get'))

    # login_user(user)
    # user.last_signin = datetime.datetime.now()
    # user.save()
    # return redirect(url_for('bp_open.sign_up'))
