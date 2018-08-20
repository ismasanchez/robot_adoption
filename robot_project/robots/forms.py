from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):

    name = StringField('Name of Robot:', validators=[DataRequired()])
    submit = SubmitField('Add Robot')
