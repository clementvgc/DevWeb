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
TP3
Création du fichier index.html dans le dossier templates
Modification de la vue index dans le fichier views.py
Création du fichier style.css dans le dossier static 
Implémentation du code HTML qui permet d'appliquer le CSS dans index.html
Modification de la vue about et contact dans views.py
Création de about.html et contact.html
Modification de style.css
Test de l'appli, tout fonctionne bien
TP4
Création de base.html
Modification de index.html, about.html et contact.html afin d'ajoute le template qui évite les répétitions de code
Ajout des images dans static/images/
Modification de views.py, notamment de l'index et ajout de la fonction getAuteurs()

# Séance 4 :
Modification de index.html car un de mes url_for() était mauvais
Création de livres_list.html
Ajout de la fonction getLivres() dans views.py
Prise en main de bootstrap
Modification de app.py pour lancer avec Bootstrap
Remplacement complet du code de base.html
Modification de style.css
Fin TP4

# Séance 5 :
TP5
Téléchargement de WTForms dans Flask
Création de forms.py
Ajout d'une fonction dans views.py pour modifier un auteur
Création de auteur_update.html
Ajout d'une fonction pour sauvegarder les modifications d'un auteur et d'une autre pour voir si les modifications ont bien été sauvegardées
Création de auteur_view.html
Ajout de plusieurs fonctions dans views.py et création/modification de plusieurs teamplates
On a désormais la possibilité de voir, éditer et supprimer des auteurs
Possibilité de voir et éditer les livres
Fin TP5

# Séance 6 :
TP6
Ajout de la classe User dans models.py
Ajout de la fonction syncdb dans commands.py
Ajout de commandes pour créer un utilisateur et changer son mot de passe dans commands.py
Modification de app.py pour activer le plugin
Ajout de code dans models.py 
Création d'un formulaire pour permettre à un utilisateur de s’authentifier dans forms.py
Création de login.html
Modification de base.html pour que l'utilisateur sache qu'il est connecté
Ajout d'une vue logout pour que la déconnexion fonctionne dans views.py
Modification de auteur_list.html pour que la page d'édition et de suppression soit accessible que aux utilisateurs authentifiés
Ajout de @login_required devant toutes les vues qui ne sont pas fait pour consulter
Mise en place de la redirection automatique dans app.py
Ajout d'une ligne dans la classe LoginForm dans forms.py et modification de la vue login dans views.py pour se souvenir de la page précédente
Fin TP6
TP7
Création de conftest.py
Création du répertoire unit avec les fichiers __init__.py et test_models_auteur.py

# Séance 7 :
Création du fichier .coveragerc
Création de test_models_livres.py et test_models_user.py
Création du répertoire functional dans tests/ avec un fichier __init__.py vide et test_routes_auteur.py
Ajout dans test_routes_auteur.py de tous les tests nécessaire pour tester toutes les routes en référence avec auteur
Création de test_forms_auteur.py et ajout de tests dedans permettant de tester les méthodes POST pour auteur
Ensuite, j'ai fait la même chose pour les livres en créant les fichiers test_routes_livres.py et test_forms_livres.py
Et pareil pour les méthodes diverses tels que index, about, contact et logout dans test_routes_misc.py





