from flask import Flask
from config import Config
from flask_cors import CORS

cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cors.init_app(app)

    # Evaluate Level
    from app.evaluate import bp as evaluate_bp
    app.register_blueprint(evaluate_bp)

    # Main Page binding
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Search Page binding
    from app.search import bp as search_bp
    app.register_blueprint(search_bp)

    # Add Page binding
    from app.add import bp as add_bp
    app.register_blueprint(add_bp)

    # Identify Skill level binding
    from app.identify import bp as identify_bp
    app.register_blueprint(identify_bp)

    # Results Feature binding
    from app.results import bp as results_bp
    app.register_blueprint(results_bp)

    # Your repository binding
    from app.repository import bp as repository_bp
    app.register_blueprint(repository_bp)

    # Comments to a resource binding
    from app.comments import bp as comments_bp
    app.register_blueprint(comments_bp)

    # Api endpoints binding
    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
