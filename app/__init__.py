from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from.routes import routes_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://teste:teste2024@localhost/teste'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(routes_bp)

    return app
