from flask import render_template
from app.repository import bp


@bp.route('/repository/')
def repository():
    return render_template('repository/repository.html', title="Your Repository")
