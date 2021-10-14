from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class BasicForm(FlaskForm):
    searchfield = StringField("Search for tags")
    clickme = BooleanField("Click me", validators=[DataRequired()])
    submit = SubmitField("Search")
