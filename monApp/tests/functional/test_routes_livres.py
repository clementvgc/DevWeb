from monApp.app import app
from .test_routes_auteur import login

def test_livres_liste(client, testapp):
    response = client.get('/livres/')
    assert response.status_code == 200
    assert b"Les Mis\xc3\xa9rables" in response.data  

def test_livre_view(client, testapp):
    response = client.get('/livres/1/view/')
    assert response.status_code == 200
    assert b"D\xc3\xa9tails du livre" in response.data 
    assert b"Les Mis\xc3\xa9rables" in response.data

def test_livre_update_before_login(client, testapp):
    response = client.get('/livres/1/update/', follow_redirects=True)
    assert b"Se connecter" in response.data

def test_livre_update_after_login(client, testapp):
    response = login(client, "CDAL", "AIGRE", "/livres/1/update/")
    assert response.status_code == 200
    assert b"Modifier le prix du livre" in response.data

def test_livre_create_before_login(client, testapp):
    response = client.get('/livre/', follow_redirects=True)
    assert b"Se connecter" in response.data

def test_livre_create_after_login(client, testapp):
    response = login(client, "CDAL", "AIGRE", "/livre/")
    assert response.status_code == 200
    assert b"Ajouter un nouveau livre" in response.data

def test_livre_delete_before_login(client, testapp):
    response = client.get('/livres/1/delete/', follow_redirects=True)
    assert b"Se connecter" in response.data

def test_livre_delete_after_login(client, testapp):
    response = login(client, "CDAL", "AIGRE", "/livres/1/delete/")
    assert response.status_code == 200
    assert b"Supprimer le livre" in response.data