from flask import Flask
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    # app.config["SECRET_KEY"] = "aihduaoihduoia"
    app.config.from_pyfile("settings.py")
    app.static_folder = 'static'

    from website.persistence.db import init_db
    init_db(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_email):
        from website.controllers.user_controller import get_user_by_email
        return get_user_by_email(user_email)

    from .views import views
    from website.blueprints.open import bp_open
    from .mainpage import main_page
    from .synchronize import synchronize_page
    #from .adddata import add_data
    from .accountsettings import account_settings
    from website.blueprints.users import bp_users

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(bp_open, url_prefix="/")
    app.register_blueprint(bp_users, url_prefix="/")
    app.register_blueprint(main_page, url_perfix="/")
    app.register_blueprint(synchronize_page, url_perfix="/")
    #app.register_blueprint(add_data, url_prefix="/")
    app.register_blueprint(account_settings, url_prefix="/")

    return app
