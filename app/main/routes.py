from flask import render_template
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html')


@bp.route('/hello/')
def hello():
    return render_template('main/hello.html', title="Hello Page")
