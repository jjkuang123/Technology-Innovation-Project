from flask import render_template, url_for, redirect
from app.forms import NavigationForm, return_search_query
from app.comments import bp
from app.view_model import Video


@bp.route('/comments/<resource_id>', methods=['GET', 'POST'])
def comments(resource_id):
    form = NavigationForm()

    # Logic to query database to get resource from resource_id
    resource = Video(89, 'link_to_youtube')

    if form.validate_on_submit():
        query = return_search_query(form)
        return redirect(url_for('results.results', search_query=query))
    return render_template('comments/comments.html',
                           title="Comments Page", form=form, resource=resource)
