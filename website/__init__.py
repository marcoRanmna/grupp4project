from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "aihduaoihduoia"

    from .views import views
    from .auth import auth
    from .mainpage import main_page

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(main_page, url_perfix="/")

    return app
