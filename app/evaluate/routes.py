from flask import render_template, redirect, url_for, request, current_app
from app.forms import NavigationForm, return_search_query
from app.evaluate.evaluate_forms import EvaluateForm
from app.evaluate import bp


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
        understanding_1 = form_eval.understanding_1.data
        understanding_2 = form_eval.understanding_2.data
        understanding_3 = form_eval.understanding_3.data
        current_app.logger.info(
            f"{understanding_1}, {understanding_2}, {understanding_3}")

        # Lgic for rating level based on understandings

    return render_template('evaluate/evaluate.html',
                           title="Evaluate Level", form=form, form_eval=form_eval)
