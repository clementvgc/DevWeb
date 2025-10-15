from .app import app, db
from flask import render_template, request, url_for, redirect
from monApp.models import Auteur, Livre
from monApp.forms import FormAuteur, FormLivre, LoginForm
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route('/index/')
def index():
    if len(request.args) == 0:
        return render_template("index.html", title="Accueil", name="Cricri")
    else:
        param_name = request.args.get("name")
        return render_template("index.html", title="Accueil", name=param_name)

@app.route('/about/')
def about():
    return render_template("about.html", title="À propos")

@app.route('/contact/')
def contact():
    return render_template("contact.html", title="Contact", numero="07 23 34 31 28")

@app.route('/auteurs/')
def getAuteurs():
    lesAuteurs = Auteur.query.all()
    return render_template('auteurs_list.html', title="R3.01 Dev Web avec Flask", auteurs=lesAuteurs)

@app.route('/livres/')
def getLivres():
    lesLivres = Livre.query.all()
    return render_template('livres_list.html', title="Liste des livres", livres=lesLivres)

@app.route('/auteurs/<idA>/update/')
@login_required
def updateAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur(idA=unAuteur.idA , Nom=unAuteur.Nom)
    return render_template("auteur_update.html",selectedAuteur=unAuteur, updateForm=unForm)

@app.route ('/auteur/save/', methods =("POST" ,))
@login_required
def saveAuteur():
    updatedAuteur = None
    unForm = FormAuteur()
    #recherche de l'auteur à modifier
    idA = int(unForm.idA.data)
    updatedAuteur = Auteur.query.get(idA)
    #si les données saisies sont valides pour la mise à jour
    if unForm.validate_on_submit():
        updatedAuteur.Nom = unForm.Nom.data
        db.session.commit()
        return redirect(url_for('viewAuteur', idA=updatedAuteur.idA))

    return render_template("auteur_update.html",selectedAuteur=updatedAuteur, updateForm=unForm)

@app.route('/auteurs/<idA>/view/')
def viewAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur (idA=unAuteur.idA , Nom=unAuteur.Nom)
    return render_template("auteur_view.html",selectedAuteur=unAuteur, viewForm=unForm)

@app.route('/auteur/')
@login_required
def createAuteur():
    unForm = FormAuteur()
    return render_template("auteur_create.html", createForm=unForm)

@app.route ('/auteur/insert/', methods =("POST" ,))
@login_required
def insertAuteur():
    insertedAuteur = None
    unForm = FormAuteur()
    if unForm.validate_on_submit():
        insertedAuteur = Auteur(Nom=unForm.Nom.data)
        db.session.add(insertedAuteur)
        db.session.commit()
        insertedId = Auteur.query.count()
        return redirect(url_for('viewAuteur', idA=insertedId))
    return render_template("auteur_create.html", createForm=unForm)

@app.route('/auteurs/<idA>/delete/')
@login_required
def deleteAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur(idA=unAuteur.idA, Nom=unAuteur.Nom)
    return render_template("auteur_delete.html",selectedAuteur=unAuteur, deleteForm=unForm)

@app.route ('/auteur/erase/', methods =("POST" ,))
@login_required
def eraseAuteur():
    deletedAuteur = None
    unForm = FormAuteur()
    #recherche de l'auteur à supprimer
    idA = int(unForm.idA.data)
    deletedAuteur = Auteur.query.get(idA)
    #suppression
    db.session.delete(deletedAuteur)
    db.session.commit()
    return redirect(url_for('getAuteurs'))

@app.route('/livres/<idL>/view/')
def viewLivre(idL):
    unLivre = Livre.query.get(idL)
    unForm = FormLivre(idL=unLivre.idL, Titre=unLivre.Titre, Prix=unLivre.Prix, 
                       Url=unLivre.Url, Img=unLivre.Img, auteur_id=unLivre.auteur_id)
    unForm.auteur_id.choices = [(a.idA, a.Nom) for a in Auteur.query.all()]
    return render_template("livre_view.html", selectedLivre=unLivre, viewForm=unForm)


@app.route('/livres/<idL>/update/')
@login_required
def updateLivre(idL):
    unLivre = Livre.query.get(idL)
    unForm = FormLivre(idL=unLivre.idL, Titre=unLivre.Titre, Prix=unLivre.Prix, 
                       Url=unLivre.Url, Img=unLivre.Img, auteur_id=unLivre.auteur_id)
    unForm.auteur_id.choices = [(a.idA, a.Nom) for a in Auteur.query.all()]
    return render_template("livre_update.html", selectedLivre=unLivre, updateForm=unForm)

@app.route('/livre/save/', methods=("POST",))
@login_required
def saveLivre():
    updatedLivre = None
    unForm = FormLivre()
    unForm.auteur_id.choices = [(a.idA, a.Nom) for a in Auteur.query.all()]
    idL = int(unForm.idL.data)
    updatedLivre = Livre.query.get(idL)
    if unForm.validate_on_submit():
        updatedLivre.Prix = unForm.Prix.data
        db.session.commit()
        return redirect(url_for('viewLivre', idL=updatedLivre.idL))
    return render_template("livre_update.html", selectedLivre=updatedLivre, updateForm=unForm)

@app.route('/livre/')
@login_required
def createLivre():
    unForm = FormLivre()
    unForm.auteur_id.choices = [(a.idA, a.Nom) for a in Auteur.query.all()]
    return render_template("livre_create.html", createForm=unForm)

@app.route('/livre/insert/', methods=("POST",))
@login_required
def insertLivre():
    insertedLivre = None
    unForm = FormLivre()
    unForm.auteur_id.choices = [(a.idA, a.Nom) for a in Auteur.query.all()]
    if unForm.validate_on_submit():
        insertedLivre = Livre(Titre=unForm.Titre.data, Prix=unForm.Prix.data, 
                             Url=unForm.Url.data, Img=unForm.Img.data, 
                             auteur_id=unForm.auteur_id.data)
        db.session.add(insertedLivre)
        db.session.commit()
        insertedId = Livre.query.count()
        return redirect(url_for('viewLivre', idL=insertedId))
    return render_template("livre_create.html", createForm=unForm)

@app.route('/livres/<idL>/delete/')
@login_required
def deleteLivre(idL):
    unLivre = Livre.query.get(idL)
    unForm = FormLivre(idL=unLivre.idL, Titre=unLivre.Titre, Prix=unLivre.Prix, 
                       Url=unLivre.Url, Img=unLivre.Img, auteur_id=unLivre.auteur_id)
    unForm.auteur_id.choices = [(a.idA, a.Nom) for a in Auteur.query.all()]
    return render_template("livre_delete.html", selectedLivre=unLivre, deleteForm=unForm)

@app.route('/livre/erase/', methods=("POST",))
@login_required
def eraseLivre():
    deletedLivre = None
    unForm = FormLivre()
    idL = int(unForm.idL.data)
    deletedLivre = Livre.query.get(idL)
    db.session.delete(deletedLivre)
    db.session.commit()
    return redirect(url_for('getLivres'))

@app.route("/login/", methods=("GET", "POST"))
def login():
    unForm = LoginForm()
    unUser = None
    if not unForm.is_submitted():
        unForm.next.data = request.args.get('next')
    elif unForm.validate_on_submit():
        unUser = unForm.get_authenticated_user()
        if unUser:
            login_user(unUser)
            next_url = unForm.next.data or url_for("index", name=unUser.Login)
            return redirect(next_url)
    return render_template("login.html", form=unForm)

@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('index'))

#if __name__ == "__main__":
#    app.run()