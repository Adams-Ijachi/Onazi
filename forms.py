from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class SearchForm(FlaskForm):
    url = StringField('Search', render_kw={"placeholder": "Search"}, validators=[DataRequired()])
    submit = SubmitField('Search', render_kw={"class": "btn btn-success"})