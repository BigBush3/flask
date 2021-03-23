from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('title of activity', validators=[DataRequired()])
    team_leader = StringField("Team leader", validators=[DataRequired()])
    duration = IntegerField("Duration", validators=[DataRequired()])
    collaborators = StringField('List of collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is finished')
    submit = SubmitField('Применить')