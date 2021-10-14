from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired


class AddResourceForm(FlaskForm):
    addfield = StringField("Add appropriate tags", validators=[DataRequired()])
    language = SelectField("Language", choices=[(
        "fr", "French"), ("en", "English")], validators=[DataRequired()])
    level = SelectField("Level", choices=[(
        "in1", "Intermediate 1"), ("in2", "Intermediate 2")], validators=[DataRequired()])
    understanding = IntegerRangeField("Understanding")
    usefulness = IntegerRangeField("Usefulness")
    link = StringField("Link to resource", validators=[DataRequired()])
    submit = SubmitField("Add")
