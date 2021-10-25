from flask import render_template, redirect, url_for, current_app
from flask import request, jsonify
from app.forms import NavigationForm, return_search_query
from app.evaluate.evaluate_forms import EvaluateForm
from app.evaluate import bp
import statistics

# Data Models
from app.database_logic import search_function
from app.view_model import Query, global_user


@bp.route('/evaluate/', methods=['GET', 'POST'])
@bp.route('/evaluate/<search_query>', methods=['GET', 'POST'])
def evaluate(search_query=None):
    form = NavigationForm()
    form_eval = EvaluateForm()
    if form.validate_on_submit():
        query = return_search_query(form)
        return redirect(url_for('results.results', search_query=query))

    # Logic for processing que search_query

    # Logic for rating level based on understandings
    resources = search_function(search_query)[:3]
    chosen_level = Query.get_level(search_query)

    return render_template('evaluate/evaluate.html',
                           title="Evaluate Level", form=form,
                           form_eval=form_eval,
                           chosen_level=chosen_level,
                           resources=resources)


@bp.route('/evaluate/get_understanding', methods=['POST'])
def get_understanding():

    chosen_level = int(request.form['chosenLevel'])
    understanding_1 = int(request.form['understanding1'])
    understanding_2 = int(request.form['understanding2'])
    understanding_3 = int(request.form['understanding3'])

    current_app.logger.info(
        f"{chosen_level} {understanding_1} {understanding_2} {understanding_3}")

    # Used to determine the level of the user
    level = get_appropriate_level(understanding_1, understanding_2,
                                  understanding_3, int(chosen_level))

    r = {'level': level}

    return jsonify(r)


def get_appropriate_level(under1, under2, under3, chosen_level):
    drop_level = 30
    correct_level = 70
    average = statistics.mean([under1, under2, under3])

    c = chosen_level
    if average <= drop_level:
        c = chosen_level - 1
        if c == 0:
            c = 1
    elif average >= correct_level:
        c = chosen_level + 1
        if c == 4:
            c = 3
    global_user['level'] = int(c)
    current_app.logger.info(f'MY CURRENT LEVEL IS: {c} ')
    return c
