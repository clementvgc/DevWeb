## DevWeb Clément Vignon--Chaudey

# Séance 1 :

j'ai oublié de faire mon readme lors de la première séance mais j'ai fait tout le TP1

# Séance 2 :

Début du TP2
Création de monApp.db à la racine du projet.
Installation de SQLAlchemy.
Ajout de code dans config.py, app.py
Création des tables Auteur et Livre dans models.py et de commands.py
Importation de models.py et commands.py dans __init__.py
La base de données a bien été créé à la suite de l'installation de pyyaml.
J'ai pu commencer à manipuler le shell de Flask.
J'ai ajouté la fonction __repr__(self) à la classe Livre et Auteur afin que l'affichage dans le shell soit compréhensible.
Enfin j'ai encore été dans le shell Flask en faisant des requêtes permettant de manipuler les données des tables que j'ai créé mais aussi en ajoutant/modifiant/supprimant des éléments des tables.
J'ai pu faire le TP2 en entier durant cette séance.

# Séance 3 :

Création du fichier index.html dans le dossier templates
Modification de la vue index dans le fichier views.py
Création du fichier style.css dans le dossier static 
Implémentation du code HTML qui permet d'appliquer le CSS dans index.html
Modification de la vue about et contact dans views.py
Création de about.html et contact.html
Modification de style.css
Test de l'appli, tout fonctionne bien

# Séance 4 :
Création de base.html
Modification de index.html, about.html et contact.html afin d'ajoute le template qui évite les répétitions de code
Ajout des images dans static/images/
Modification de views.py, notamment de l'index et ajout de la fonction getAuteurs()