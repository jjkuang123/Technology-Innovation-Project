from flask import render_template, redirect, url_for
from app.main import bp

# Forms
from app.main.main_forms import BasicForm
from app.forms import LoginForm
from app.view_model import set_global_user


@bp.route('/')
@bp.route('/index')
def index():
    return redirect(url_for('main.login'))
    # return render_template('main/index.html')


@bp.route('/forms', methods=['GET', 'POST'])
def forms():
    form = BasicForm()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('main/forms.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        set_global_user(form.user.data)
        return redirect(url_for('identify.identify'))
    return render_template('main/login.html', form=form)
