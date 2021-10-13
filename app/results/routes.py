from flask import render_template
from app.results import bp


@bp.route('/results/')
def results():
    return render_template('results/results.html', title="Search Results")
