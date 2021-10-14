from flask import render_template
from app.identify import bp
from app.forms import BasicResourceForm


@bp.route('/identify/', methods=['GET', 'POST'])
def identify():
    form = BasicResourceForm()
    if form.validate_on_submit:
        identifyBegin = form.searchfield.data
        print(identifyBegin)
    return render_template('identify/identify.html', title="Identify Skill Level", form=form)
