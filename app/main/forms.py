from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField('Search term', validators=[DataRequired(message="Try a name")])
    submit = SubmitField('Search')

