import click
import logging as lg
import yaml

from .app import app, db
from .models import Auteur, Livre

@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    """Creates the tables and populates them with data."""
    # Création de toutes les tables
    db.drop_all()
    db.create_all()

    # Chargement de notre jeu de données
    with open(filename, 'r') as file:
        lesLivres = yaml.safe_load(file)

    # Première passe : création de tous les auteurs
    lesAuteurs = {}
    for livre in lesLivres:
        auteur = livre["author"]
        if auteur not in lesAuteurs:
            objet = Auteur(Nom=auteur)
            db.session.add(objet)
            lesAuteurs[auteur] = objet
    db.session.commit()

    # Deuxième passe : création de tous les livres
    for livre in lesLivres:
        auteur = lesAuteurs[livre["author"]]
        objet = Livre(
            Prix=livre["price"],
            Titre=livre["title"],
            Url=livre["url"],
            Img=livre["img"],
            auteur_id=auteur.idA
        )
        db.session.add(objet)
    db.session.commit()

    lg.warning('Database initialized!')

@app.cli.command()
def syncdb():
    """Creates all missing tables . """
    db.create_all()
    lg.warning('Database synchronized!')

@app.cli.command()
@click.argument('login')
@click.argument('pwd')
def newuser(login, pwd):
    """Adds a new user"""
    from . models import User
    from hashlib import sha256
    m = sha256()
    m.update(pwd.encode())
    unUser = User(Login=login ,Password =m.hexdigest())
    db.session.add(unUser)
    db.session.commit()
    lg.warning('User ' + login + ' created!')

@app.cli.command()
@click.argument('login')
@click.argument('pwd')
def newpasswrd(login, pwd):
    """Change the password for a user"""
    from .models import User
    from hashlib import sha256
    user = User.query.filter_by(Login=login).first()
    if user is None:
        lg.warning("User " + login + " not found !")
        return None
    m = sha256()
    m.update(pwd.encode())
    user.Password = m.hexdigest()
    db.session.commit()
    lg.warning("Password for user " + login + " updated!")