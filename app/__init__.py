from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

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

    return app
