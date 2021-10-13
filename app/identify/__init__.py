from flask import Blueprint


bp = Blueprint('identify', __name__)


from app.identify import routes
