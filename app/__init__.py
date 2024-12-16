# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
import os

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
migrate = Migrate()


def create_app():
    app = Flask(__name__, static_folder="../static", template_folder="../templates")
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)

    from .models import Movie  # 延遲導入，避免循環依賴

    from .routes import main, auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
