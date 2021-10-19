from flask import render_template, redirect, url_for, current_app
from app.add import bp
from app.add.forms import AddResourceForm
from app.view_model import Video
from app.database_logic import add_function
# from app.database_logic import add_function


@bp.route('/add/', methods=['GET', 'POST'])
def add():
    form = AddResourceForm()
    if form.validate_on_submit():
        tags = form.addfield.data
        language = form.language.data
        level = form.level.data
        understanding = int(form.understanding.data)
        like = int(form.like.data)
        link = form.link.data
        current_app.logger.info(f"""
                                Tag: {tags}
                                Lng: {language}
                                Lvl: {level}
                                Und: {understanding}
                                Use: {like}
                                Lnk: {link}
                                """)

        new_resource = Video(link=link)

        add_function("Sandon Lai", language, like,
                     understanding, level, tags, new_resource)

        # current_app.logger.info("Added new resource to the database.")

    return render_template('add/add.html', title="Add Page", form=form)
