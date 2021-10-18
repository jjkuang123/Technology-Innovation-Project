from flask import render_template, url_for, redirect, current_app
from flask import request, jsonify
from app.forms import NavigationForm, return_search_query
from app.repository import bp

# Import Models
from app.view_model import Video
from app.database_logic import obtain_user_resources


@bp.route('/repository/', methods=['GET', 'POST'])
def repository():
    form = NavigationForm()

    # Logic for retrieving resources from the user
    # Ideally we would have a user linked in here and we can query according to the user
    # For now we use a test user: "Leon Wu"
    resources = obtain_user_resources("Leon Wu")

    if form.validate_on_submit():
        query = return_search_query(form)
        return redirect(url_for('results.results', search_query=query))

    return render_template('repository/repository.html',
                           title="Your Repository", form=form,
                           resources=resources)
