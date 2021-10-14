from flask import render_template, redirect, url_for, request, current_app
from app.forms import NavigationForm
from app.evaluate.evaluate_forms import EvaluateForm
from app.evaluate import bp


@bp.route('/evaluate/', methods=['GET', 'POST'])
def evaluate():
    form = NavigationForm()
    form_eval = EvaluateForm()
    if form.validate_on_submit():
        query = form.searchfield.data
        current_app.logger.info(f"Inside validated form, with query: {query}")
        return redirect(url_for('results.results', search_query=query))

    current_app.logger.info("about to validate form")
    if form_eval.validate_on_submit():
        current_app.logger.info("inside validated form")
        understanding_1 = form_eval.understanding_1.data
        understanding_2 = form_eval.understanding_2.data
        understanding_3 = form_eval.understanding_3.data
        current_app.logger.info(
            f"{understanding_1}, {understanding_2}, {understanding_3}")

    # return render_template('results/results.html', title="Results Page", form=form)
    return render_template('evaluate/evaluate.html', title="Evaluate Level", form=form, form_eval=form_eval)
