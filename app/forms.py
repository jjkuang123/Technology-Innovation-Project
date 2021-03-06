from app import evaluate
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired
from app.view_model import Query


class NavigationForm(FlaskForm):
    searchfield = StringField("Search using tags", render_kw={
                              'placeholder': 'Search for comma separated tags'}, validators=[DataRequired()])
    language = SelectField("Language", choices=[(
        "French", "French"), ("English", "English"), ("Mandarin", "Mandarin"), ("Spanish", "Spanish")], validators=[DataRequired()])
    level = SelectField("Level", choices=[(
        "Intermediate 1", "Intermediate 1"), ("Intermediate 2", "Intermediate 2"), ("Intermediate 3", "Intermediate 3")], validators=[DataRequired()])
    submit = SubmitField("Search")


class BasicResourceForm(NavigationForm):
    evaluate = SubmitField("Begin Evaluation")


class CommentForm(FlaskForm):
    comment_box = TextAreaField("Leave a comment", validators=[
                                DataRequired()], render_kw={'class': 'comment-box'})
    submit = SubmitField("Comment", render_kw={'class': 'comment-button'})


class LoginForm(FlaskForm):
    user = SelectField(
        "Choose your user", choices=[("Gil", "Gil"), ("Yan", "Yan"), ("Willian", "Willian"), ("Sandon Lai", "Sandon Lai"), ("Leon Wu", "Leon Wu"), ("Jero Someone", "Jero Someone"),
                                     ("Jacky Kuang", "Jacky Kuang")], validators=[DataRequired()])
    submit = SubmitField("Login")


def return_search_query(form: NavigationForm) -> str:
    searchResult = form.searchfield.data
    level = form.level.data
    language = form.language.data
    query = Query(searchResult, level, language)
    return query.get_my_query()
