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