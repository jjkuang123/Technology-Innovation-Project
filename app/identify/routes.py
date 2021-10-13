from flask import render_template
from app.identify import bp


@bp.route('/identify/')
def identify():
    return render_template('identify/identify.html', title="Identify Skill Level")
