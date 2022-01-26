from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "aihduaoihduoia"

    from .views import views
    from .auth import auth
    from .mainpage import main_page
    from .synchronize import synchronize_page
    from .adddata import add_data
    from .accountsettings import account_settings

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(main_page, url_perfix="/")
    app.register_blueprint(synchronize_page, url_perfix="/")
    app.register_blueprint(add_data, url_prefix="/")
    app.register_blueprint(account_settings, url_prefix="/")

    return app
