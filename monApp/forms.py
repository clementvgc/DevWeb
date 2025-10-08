from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, HiddenField, PasswordField
from wtforms.validators import DataRequired
from .models import User
from hashlib import sha256

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

class LoginForm(FlaskForm):
    Login = StringField('Identifiant')
    Password = PasswordField('Mot de passe')
    next = HiddenField()

    def get_authenticated_user(self):
        unUser = User.query.get(self.Login.data)
        if unUser is None:
            return None
        m = sha256()
        m.update(self.Password.data.encode())
        passwd = m.hexdigest()
        return unUser if passwd == unUser.Password else None

