import os
from flask import Flask
from data_table import db
from dashboard.routes import dashboard_bp


def make_app():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    template_dir = os.path.join(base_dir, "templates")

    app = Flask(__name__, template_folder=template_dir)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///engine_data_complete.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.register_blueprint(dashboard_bp)

    return app


