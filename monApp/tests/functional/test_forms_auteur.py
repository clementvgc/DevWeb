from monApp.models import Auteur
from monApp import db
from monApp.tests.functional.test_routes_auteur import login

def test_auteur_save_success(client, testapp):
    idA = 1

    login(client, "CDAL", "AIGRE", "/auteur/save/")
    response = client.post(
        "/auteur/save/",
        data={"idA": idA, "Nom": "Alexandre Dumas"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert f"/auteurs/{idA}/view/" in response.request.path
    assert b"Alexandre Dumas" in response.data  

    with testapp.app_context():
        auteur_modifie = db.session.get(Auteur, idA)
        assert auteur_modifie.Nom == "Alexandre Dumas"

def test_auteur_insert_success(client, testapp):
    login(client, "CDAL", "AIGRE", "/auteur/insert/")

    response = client.post("/auteur/insert/",
                           data={"Nom": "Jules Verne"},
                           follow_redirects=True)

    assert response.status_code == 200
    assert b"Consultation de l'auteur Jules Verne" in response.data

    with testapp.app_context():
        nouvel_auteur = db.session.query(Auteur).filter_by(Nom="Jules Verne").first()
        assert nouvel_auteur is not None
        assert nouvel_auteur.Nom == "Jules Verne"