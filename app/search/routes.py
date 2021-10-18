from flask import render_template, current_app, redirect, url_for
from app.search import bp
from app.forms import NavigationForm, return_search_query
from app.database_logic import search_function


@bp.route('/search/', methods=['GET', 'POST'])
def search():
    form = NavigationForm()
    if form.validate_on_submit():
        query = return_search_query(form)

        return redirect(url_for('results.results', search_query=query))
    return render_template('search/search.html', title="Search Page",
                           form=form)
