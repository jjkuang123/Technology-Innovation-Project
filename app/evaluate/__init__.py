from flask import Blueprint


bp = Blueprint('evaluate', __name__)


from app.evaluate import routes
