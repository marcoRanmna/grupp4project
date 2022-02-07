from flask import Blueprint, render_template, request, flash, redirect, url_for, make_response
from website.controllers.user_controller import create_user, signin_user, verify_user
from flask_login import current_user

bp_open = Blueprint("bp_open", __name__)


@bp_open.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@bp_open.route("/login", methods=["POST"])
def login_post():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if not verify_user(email, password):
            flash("Error")
            return redirect(url_for("bp_open.login"))
        signin_user(email)
        user_id = str(current_user._id).encode('utf-8')
        resp = make_response(redirect(url_for('main.main')))
        resp.set_cookie('user_id', user_id)
        return resp
        #return redirect(url_for("bp.open.signup_get"))


@bp_open.route("/sign-up", methods=["GET"])
def signup_get():
    return render_template("sign_up.html")


@bp_open.route("/sign-up", methods=["POST"])
def sign_up():
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
        create_user(first_name, last_name, email, password1)
        flash("Account was created.", category="success")
        return redirect(url_for("bp_open.login"))


# @bp_open.route('/login')
# def signin_post():
#     email = request.form.get('email')
#     print('hello')
#     signin_user(email)
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
