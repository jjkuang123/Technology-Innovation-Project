from flask import render_template, url_for, redirect
from app.identify import bp
from app.forms import BasicResourceForm, return_search_query


@bp.route('/identify/', methods=['GET', 'POST'])
def identify():
    form = BasicResourceForm()
    if form.validate_on_submit():
        query = return_search_query(form)
        return redirect(url_for('evaluate.evaluate', search_query=query))
    return render_template('identify/identify.html', title="Identify Skill Level", form=form)
