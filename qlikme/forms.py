from flask_wtf import FlaskForm
from wtforms import SelectField, TextField, SubmitField

class QlikmeForm(FlaskForm):
    name = TextField("Name")
    color = TextField("Favorite Color")
    pet = SelectField("Favorite Pet", choices=[('Cat', 'Cats'), ('Dog', 'Dogs')])
    submit = SubmitField("Submit")
