from flask import render_template, redirect, url_for, request, current_app
from app.forms import NavigationForm
from app.results import bp


@bp.route('/results/', methods=['GET', 'POST'])  # Empty query
# Query with a search
@bp.route('/results/<search_query>', methods=['GET', 'POST'])
def results(search_query=None):
    form = NavigationForm()
    current_app.logger.info(f"results with a query of {search_query}")
    # If someone presses the submit on the form
    # it should redirect to new results
    # if form.validate_on_submit:
    #     query = form.searchfield.data
    #     current_app.logger.info(f"query with {query} tags")
    #     return redirect(url_for('results.results', search_query=query))

    # if search_query:
    #     current_app.logger.info("GET method")
    #     results = ['TODO', 'PLACE_HOLDER', 'RESULTS']
    #     return render_template('results/results.html',
    #                            title="Search Results", results=results, form=form)

    # # TODO: Maybe show empty results page instead or something
    # return render_template('results/results.html', title="Search Results", results=results, form=form)
    if form.validate_on_submit():
        query = form.searchfield.data
        current_app.logger.info(f"Inside validated form, with query: {query}")
        return redirect(url_for('results.results', search_query=query))

    return render_template('results/results.html', title="Results Page", form=form)
