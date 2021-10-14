from flask import render_template
from app.search import bp
from app.forms import BasicResourceForm


@bp.route('/search/', methods=['GET', 'POST'])
def search():
    form = BasicResourceForm()
    if form.validate_on_submit:
        searchResult = form.searchfield.data
        print(searchResult)
    return render_template('search/search.html', title="Search Page", form=form)
