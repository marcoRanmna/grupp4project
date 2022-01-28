from flask import Blueprint

bp_users = Blueprint("bp_users", __name__)


@bp_users.route("/logout")
def logout():
    return "<p>Logout</p>"
