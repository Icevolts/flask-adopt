from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,IntegerField,TextAreaField,BooleanField
from wtforms.validators import InputRequired,NumberRange,URL,Optional

class AddPetForm(FlaskForm):
    '''Form to add a pet to the website'''
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('cat', 'Cat'),('dog', 'Dog'),('porcupine', 'Porcupine')], validators=[InputRequired()])
    photo_url = StringField('Photo URL',validators=[Optional(), URL()])
    age = IntegerField('Age',validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes',validators=[Optional()])

class EditPetForm(FlaskForm):
    '''Form to edit info on a specified pet'''
    photo_url = StringField('Photo URL',validators=[Optional(), URL()])
    notes = TextAreaField('Notes',validators=[Optional()])
    available = BooleanField('Available?')