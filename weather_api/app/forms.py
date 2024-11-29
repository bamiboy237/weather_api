from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class WeatherForm(FlaskForm):
    cityname = StringField('Enter City name...', validators=[DataRequired()])
    submit = SubmitField('Select')