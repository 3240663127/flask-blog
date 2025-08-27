from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from app.routes import register_routes
from app.extensions import db

def create_app(config_name="default"):
    app = Flask(__name__)

    app.config.from_object(config[config_name])


    db.init_app(app)
    with app.app_context():
        db.create_all()

    register_routes(app)

    return app


