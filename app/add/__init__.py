from flask import Blueprint


bp = Blueprint('add', __name__)


from app.add import routes
