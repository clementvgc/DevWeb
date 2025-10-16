from .app import app, db
from flask import render_template, request, url_for, redirect, flash
from monApp.models import Auteur, Livre
from monApp.forms import FormAuteur, FormLivre, LoginForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html", title="Accueil")

@app.route('/about/')
def about():
    return render_template("about.html", title="À propos")

@app.route('/contact/')
def contact():
    return render_template("contact.html", title="Contact", numero="07 23 34 31 28")

@app.route('/auteurs/')
def getAuteurs():
    query = request.args.get('q', '')
    if query:
        lesAuteurs = db.session.execute(db.select(Auteur).filter(Auteur.Nom.ilike(f'%{query}%'))).scalars().all()
    else:
        lesAuteurs = db.session.execute(db.select(Auteur)).scalars().all()
    return render_template('auteurs_list.html', title="Liste des Auteurs", auteurs=lesAuteurs, query=query)

@app.route('/livres/')
def getLivres():
    query = request.args.get('q', '')
    if query:
        lesLivres = db.session.execute(
            db.select(Livre).filter(Livre.Titre.ilike(f'%{query}%'))
        ).scalars().all()
    else:
        lesLivres = db.session.execute(db.select(Livre)).scalars().all()
        
    return render_template('livres_list.html', title="Liste des livres", livres=lesLivres, query=query)

@app.route('/auteurs/<idA>/update/')
@login_required
def updateAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur(idA=unAuteur.idA , Nom=unAuteur.Nom)
    return render_template("auteur_update.html",selectedAuteur=unAuteur, updateForm=unForm)

@app.route ('/auteur/save/', methods =("POST" ,))
@login_required
def saveAuteur():
    idA = int(request.form['idA'])
    updatedAuteur = Auteur.query.get(idA)
    unForm = FormAuteur(request.form)

    if unForm.validate_on_submit():
        updatedAuteur.Nom = unForm.Nom.data
        db.session.commit()
        flash(f"L'auteur '{updatedAuteur.Nom}' a été mis à jour.", 'success')
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
    unForm = FormAuteur()
    if unForm.validate_on_submit():
        nom_auteur = unForm.Nom.data
        existing_auteur = db.session.execute(db.select(Auteur).filter(Auteur.Nom.ilike(nom_auteur))).scalar_one_or_none()
        
        if existing_auteur:
            flash(f"L'auteur '{nom_auteur}' existe déjà.", 'danger')
            return redirect(url_for('createAuteur'))

        insertedAuteur = Auteur(Nom=nom_auteur)
        db.session.add(insertedAuteur)
        db.session.commit()
        flash(f"L'auteur '{insertedAuteur.Nom}' a été créé avec succès.", 'success')
        return redirect(url_for('viewAuteur', idA=insertedAuteur.idA))
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
    idA = int(request.form['idA'])
    deletedAuteur = Auteur.query.get(idA)
    
    if deletedAuteur.livres.count() > 0:
        flash(f"L'auteur '{deletedAuteur.Nom}' et tous ses livres ont été supprimés.", 'warning')
    else:
        flash(f"L'auteur '{deletedAuteur.Nom}' a été supprimé.", 'success')

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
    idL = int(request.form['idL'])
    updatedLivre = Livre.query.get(idL)
    unForm = FormLivre(request.form)
    if unForm.Prix.validate(unForm):
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
    unForm = FormLivre()
    unForm.auteur_id.choices = [(a.idA, a.Nom) for a in db.session.execute(db.select(Auteur).order_by(Auteur.Nom)).scalars()]
    if unForm.validate_on_submit():
        titre = unForm.Titre.data
        auteur_id = unForm.auteur_id.data
        existing_livre = db.session.execute(db.select(Livre).filter_by(Titre=titre, auteur_id=auteur_id)).scalar_one_or_none()

        if existing_livre:
            flash(f"Le livre '{titre}' existe déjà pour cet auteur.", 'danger')
            return redirect(url_for('createLivre'))

        auteur = db.session.get(Auteur, auteur_id)
        insertedLivre = Livre(Titre=titre, Prix=unForm.Prix.data,
                             Url=unForm.Url.data, Img=unForm.Img.data,
                             auteur=auteur)
        db.session.add(insertedLivre)
        db.session.commit()
        flash(f"Le livre '{insertedLivre.Titre}' a été ajouté avec succès.", 'success')
        return redirect(url_for('viewLivre', idL=insertedLivre.idL))
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

if __name__ == "__main__":
    app.run()