from app import evaluate
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class BasicResourceForm(FlaskForm):
    searchfield = StringField("Search using tags", validators=[DataRequired()])
    language = SelectField("Language", choices=[(
        "fr", "French"), ("en", "English")], validators=[DataRequired()])
    level = SelectField("Level", choices=[(
        "in1", "Intermediate 1"), ("in2", "Intermediate 2")], validators=[DataRequired()])
    submit = SubmitField("Search")
    evaluate = SubmitField("Begin Evaluation")
