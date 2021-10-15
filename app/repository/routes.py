from flask import render_template, url_for, redirect
from app.forms import NavigationForm, return_search_query
from app.repository import bp


@bp.route('/repository/', methods=['GET', 'POST'])
def repository():
    form = NavigationForm()
    if form.validate_on_submit():
        query = return_search_query(form)
        return redirect(url_for('results.results', search_query=query))
    return render_template('repository/repository.html',
                           title="Your Repository", form=form)
