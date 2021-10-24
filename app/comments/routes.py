from flask import render_template, url_for, redirect
from flask.globals import current_app
from app.forms import CommentForm, NavigationForm, return_search_query
from app.comments import bp
from app.view_model import Video
from app.database_logic import obtain_resource_object, obtain_comments, post_comments


@bp.route('/comments/<resource_id>', methods=['GET', 'POST'])
def comments(resource_id):
    form = NavigationForm()
    comment_form = CommentForm()

    user = 'Sandon Lai'

    # Logic to query database to get resource from resource_id
    resource = obtain_resource_object(resource_id)
    comments = obtain_comments(resource_id)

    if form.validate_on_submit():
        query = return_search_query(form)
        return redirect(url_for('results.results', search_query=query))

    if comment_form.validate_on_submit():
        post_comments(comment_form.comment_box.data, user, int(resource_id))
        return redirect(url_for('comments.comments', resource_id=resource_id))

    return render_template('comments/comments.html',
                           title="Comments Page", form=form, resource=resource,
                           comment_form=comment_form, comments=comments)
