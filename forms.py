from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(),
                                                 AnyOf(values=['dog', 'Dog', 'cat', 'Cat', 'porcupine', 'Porcupine'], 
                                         message='Enter dog, cat or porcupine!')])
    photo_url = URLField("Photo URL", validators=[Optional(), URL(message="Please enter a valid URL!")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    photo_url = URLField("Photo URL", validators=[Optional(), URL(message="Please enter a valid URL!")])
    notes = StringField("Notes")
    available = BooleanField("Available")