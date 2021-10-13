from flask import render_template
from app.evaluate import bp


@bp.route('/evaluate/')
def evaluate():
    return render_template('evaluate/evaluate.html', title="Evaluate Level")
