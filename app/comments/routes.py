from flask import render_template
from app.comments import bp


@bp.route('/comments/')
def comments():
    return render_template('comments/comments.html', title="Comments Page")
