from flask import Blueprint, render_template

profile_preference1 = Blueprint("profilepreference1", __name__)


@profile_preference1.route("/profile-preference", methods=["GET", "POST"])
def profile_preference():
    return render_template("profilepreference.html")
