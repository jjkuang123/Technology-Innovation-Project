from flask import Blueprint


bp = Blueprint('repository', __name__)


from app.repository import routes
