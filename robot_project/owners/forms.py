from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AddOwnerForm(FlaskForm):

    name = StringField('Name of Owner:  ', validators=[DataRequired()])
    robot_id = SelectField('Id of Robot:  ', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add Owner')
