from flask import Blueprint, render_template

account_settings = Blueprint("accountsettings", __name__)


@account_settings.route("/account-settings", methods=["GET", "POST"])
def accountsettings():
    return render_template("accountsettings.html")
