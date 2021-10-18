from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired


class AddResourceForm(FlaskForm):
    addfield = StringField("Add appropriate tags", validators=[DataRequired()])
    language = SelectField("Language", choices=[(
        "French", "French"), ("English", "English")], validators=[DataRequired()])
    level = SelectField("Level", choices=[(
        "Intermediate 1", "Intermediate 1"), ("Intermediate 2", "Intermediate 2")], validators=[DataRequired()])
    understanding = IntegerRangeField("Understanding")
    like = IntegerRangeField("Like")
    link = StringField("Link to resource", validators=[DataRequired()])
    submit = SubmitField("Add")
