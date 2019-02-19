from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search_item = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Search Books"})
    search = SubmitField('Search')
