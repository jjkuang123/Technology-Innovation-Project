from flask import Blueprint


bp = Blueprint('results', __name__)


from app.results import routes