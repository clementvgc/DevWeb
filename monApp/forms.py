from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, HiddenField
from wtforms.validators import DataRequired

class FormAuteur(FlaskForm):
    idA = HiddenField('idA')
    Nom = StringField('Nom', validators=[DataRequired()])

class FormLivre(FlaskForm):
    idL = HiddenField('idL')
    Titre = StringField('Titre', validators=[DataRequired()])
    Prix = FloatField('Prix', validators=[DataRequired()])
    Url = StringField('URL', validators=[DataRequired()])
    Img = StringField('Image', validators=[DataRequired()])
    auteur_id = SelectField('Auteur', coerce=int, validators=[DataRequired()])