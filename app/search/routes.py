from flask import render_template
from app.search import bp


@bp.route('/search/')
def search():
    return render_template('search/search.html', title="Search Page")
