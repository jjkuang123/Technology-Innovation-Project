from flask import render_template, redirect, url_for, request, current_app
from app.forms import NavigationForm, return_search_query
from app.results import bp
from app.database_logic import search_function

# Data Models
from app.view_model import Video, global_user


@bp.route('/results/', methods=['GET', 'POST'])  # Empty query
# Query with a search
@bp.route('/results/<search_query>', methods=['GET', 'POST'])
def results(search_query=None):
    form = NavigationForm()

    # Logic for retrieving the resources based on the query
    resources = search_function(search_query)

    if form.validate_on_submit():
        query = return_search_query(form)
        return redirect(url_for('results.results', search_query=query))

    return render_template('results/results.html', title="Results Page",
                           form=form, resources=resources, global_user=global_user)
