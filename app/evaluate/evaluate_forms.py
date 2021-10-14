from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired


class EvaluateForm(FlaskForm):
    understanding_1 = IntegerRangeField("Understanding")
    understanding_2 = IntegerRangeField("Understanding")
    understanding_3 = IntegerRangeField("Understanding")
    submit = SubmitField("Tell me my level")

    def get_understanding(self, number):
        if number == 1:
            return self.understanding_1
        elif number == 2:
            return self.understanding_2
        else:
            return self.understanding_3
