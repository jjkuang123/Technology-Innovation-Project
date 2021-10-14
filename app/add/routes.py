from flask import render_template, redirect, url_for
from app.add import bp
from app.add.forms import AddResourceForm


@bp.route('/add/', methods=['GET', 'POST'])
def add():
    form = AddResourceForm()
    if form.validate_on_submit:
        searchResult = form.searchfield.data
        print(searchResult)
    return render_template('add/add.html', title="Add Page", form=form)
