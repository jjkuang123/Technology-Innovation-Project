from flask import render_template, redirect, url_for
from app.add import bp
from app.add.forms import AddResourceForm


@bp.route('/add/', methods=['GET', 'POST'])
def add():
    form = AddResourceForm()
    if form.validate_on_submit:
        addResult = form.addfield.data
        print(addResult)
    return render_template('add/add.html', title="Add Page", form=form)
