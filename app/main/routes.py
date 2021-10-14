from flask import render_template, redirect, url_for
from app.main import bp

# Forms
from app.main.forms import BasicForm


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html')


@bp.route('/forms', methods=['GET', 'POST'])
def forms():
    form = BasicForm()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('main/forms.html', form=form)
