from monApp.models import Livre, Auteur
from monApp.app import db
from .test_routes_auteur import login

def test_livre_save_success(client, testapp):
    login(client, "CDAL", "AIGRE", "/livre/save/")

    with testapp.app_context():
        livre = db.session.get(Livre, 1)

    response = client.post("/livre/save/",
                           data={
                               "idL": livre.idL,
                               "Titre": livre.Titre,
                               "Url": livre.Url,
                               "Img": livre.Img,
                               "auteur_id": livre.auteur_id,
                               "Prix": "9.99" 
                           },
                           follow_redirects=True)

    assert response.status_code == 200
    assert "/livres/1/view/" in response.request.path
    assert b"9.99" in response.data

    with testapp.app_context():
        livre_modifie = db.session.get(Livre, 1)
        assert livre_modifie.Prix == 9.99

def test_livre_insert_success(client, testapp):
    login(client, "CDAL", "AIGRE", "/livre/insert/")

    response = client.post("/livre/insert/",
                           data={
                               "Titre": "Vingt mille lieues sous les mers",
                               "Prix": "12.50",
                               "Url": "http://example.com/20000",
                               "Img": "image2.jpg",
                               "auteur_id": 1
                           },
                           follow_redirects=True)

    assert response.status_code == 200
    assert b"Vingt mille lieues sous les mers" in response.data

    with testapp.app_context():
        nouveau_livre = db.session.query(Livre).filter_by(Titre="Vingt mille lieues sous les mers").first()
        assert nouveau_livre is not None
        assert nouveau_livre.Prix == 12.50

def test_livre_erase_success(client, testapp):
    login(client, "CDAL", "AIGRE", "/livre/erase/")

    with testapp.app_context():
        auteur = db.session.get(Auteur, 1)
        livre_a_supprimer = Livre(Titre="Livre a effacer", Prix=1.0, Url="url", Img="img", auteur=auteur)
        db.session.add(livre_a_supprimer)
        db.session.commit()
        idL = livre_a_supprimer.idL
    
    response = client.post("/livre/erase/",
                           data={"idL": idL},
                           follow_redirects=True)

    assert response.status_code == 200
    assert "/livres/" in response.request.path
    assert b"Livre a effacer" not in response.data

    with testapp.app_context():
        livre_supprime = db.session.get(Livre, idL)
        assert livre_supprime is None