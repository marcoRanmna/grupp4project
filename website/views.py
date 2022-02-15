from flask import Blueprint, render_template
from website.controllers.user_controller import get_user_data

views = Blueprint("views", __name__)


@views.route("/")
def home():
    user_data = get_user_data()
    if not user_data:
        user_data = user_data.__dict__
        user_data["_id"] = str(user_data["_id"])
    data = [
        ("13-02-2022", 1597),
        ("14-02-2022", 1456),
        ("15-02-2022", 1908),
        ("16-02-2022", 896),
        ("17-02-2022", 766),
        ("18-02-2022", 321),
        ("19-02-2022", 1100),
        ("20-02-2022", 1478),
    ]

    labels = []
    values = []
    for row in data:
        labels.append(row[0])
        values.append(row[1])

    return render_template("home.html", labels=user_data["date"], values=values)
