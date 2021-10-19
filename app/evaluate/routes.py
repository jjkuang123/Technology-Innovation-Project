from flask import render_template, redirect, url_for, request, current_app
from app.forms import NavigationForm, return_search_query
from app.evaluate.evaluate_forms import EvaluateForm
from app.evaluate import bp
import statistics

# Data Models
from app.database_logic import search_function
from app.view_model import Query


@bp.route('/evaluate/', methods=['GET', 'POST'])
@bp.route('/evaluate/<search_query>', methods=['GET', 'POST'])
def evaluate(search_query=None):
    form = NavigationForm()
    form_eval = EvaluateForm()
    if form.validate_on_submit():
        query = return_search_query(form)
        return redirect(url_for('results.results', search_query=query))

    # Logic for processing que search_query

    current_app.logger.info("about to validate form")
    if form_eval.validate_on_submit():
        current_app.logger.info("inside validated form")
        # chosen_level = search_query
        chosen_level = Query.get_level(search_query)
        understanding_1 = form_eval.understanding_1.data
        understanding_2 = form_eval.understanding_2.data
        understanding_3 = form_eval.understanding_3.data
        current_app.logger.info(
            f"{understanding_1}, {understanding_2}, {understanding_3}")

        # Used to determine the level of the user
        get_appropriate_level(understanding_1, understanding_2,
                              understanding_3, int(chosen_level))

        # Logic for rating level based on understandings
        resources = search_function(search_query)[:3]

    return render_template('evaluate/evaluate.html',
                           title="Evaluate Level", form=form, form_eval=form_eval, resources=resources)


def get_appropriate_level(under1, under2, under3, chosen_level):
    drop_level = 30
    correct_level = 70
    average = statistics.mean([under1, under2, under3])

    if average <= drop_level:
        return chosen_level - 1
    elif average >= correct_level:
        return chosen_level + 1
    else:
        return chosen_level
