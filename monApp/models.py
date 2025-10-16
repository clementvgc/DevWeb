from .app import db, login_manager
from flask_login import UserMixin

class Auteur(db.Model):
    idA = db.Column(db.Integer, primary_key=True)
    Nom = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, Nom):
        self.Nom = Nom

    def __repr__(self):
        return f"<Auteur ({self.idA}) {self.Nom}>"

class Livre(db.Model):
    idL = db.Column(db.Integer, primary_key=True)
    Titre = db.Column(db.String(128), nullable=False)
    Prix = db.Column(db.Float)
    Url = db.Column(db.String(256))
    Img = db.Column(db.String(256))
    auteur_id = db.Column(db.Integer, db.ForeignKey('auteur.idA'), nullable=False)
    auteur = db.relationship("Auteur", backref=db.backref("livres", lazy="dynamic", cascade="all, delete-orphan"))

    __table_args__ = (db.UniqueConstraint('Titre', 'auteur_id', name='_titre_auteur_uc'),)

    def __init__(self, Titre, Prix, Url, Img, auteur):
        self.Titre = Titre
        self.Prix = Prix
        self.Url = Url
        self.Img = Img
        self.auteur = auteur

    def __repr__(self):
        return f"<Livre ({self.idL}) {self.Titre}>"

class User(db.Model, UserMixin):
    Login = db.Column(db.String(50), primary_key=True)
    Password = db.Column(db.String(64))
    
    def get_id(self):
        return self.Login

@login_manager.user_loader
def load_user(username):
    return db.session.get(User, username)