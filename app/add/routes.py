from flask import render_template
from app.add import bp


@bp.route('/add/')
def add():
    return render_template('add/add.html', title="Add Page")
