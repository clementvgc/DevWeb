from monApp.app import app
from .test_routes_auteur import login

def test_livres_liste(client):
    """Teste que la liste des livres s'affiche bien."""
    response = client.get('/livres/')
    assert response.status_code == 200
    assert b"Les Mis\xc3\xa9rables" in response.data  

def test_livre_view(client):
    """Teste la vue de consultation d'un livre."""
    response = client.get('/livres/1/view/')
    assert response.status_code == 200
    assert b"D\xc3\xa9tails du livre" in response.data 
    assert b"Les Mis\xc3\xa9rables" in response.data

def test_livre_update_before_login(client):
    """Teste la redirection si on essaie de modifier un livre sans être connecté."""
    response = client.get('/livres/1/update/', follow_redirects=True)
    assert b"Se connecter" in response.data

def test_livre_update_after_login(client):
    """Teste que la page de modification de livre s'affiche bien une fois connecté."""
    response = login(client, "CDAL", "AIGRE", "/livres/1/update/")
    assert response.status_code == 200
    assert b"Modifier le prix du livre" in response.data

def test_livre_create_before_login(client):
    """Teste la redirection si on essaie de créer un livre sans être connecté."""
    response = client.get('/livre/', follow_redirects=True)
    assert b"Se connecter" in response.data

def test_livre_create_after_login(client):
    """Teste que la page de création de livre s'affiche bien une fois connecté."""
    response = login(client, "CDAL", "AIGRE", "/livre/")
    assert response.status_code == 200
    assert b"Ajouter un nouveau livre" in response.data

def test_livre_delete_before_login(client):
    """Teste la redirection si on essaie de supprimer un livre sans être connecté."""
    response = client.get('/livres/1/delete/', follow_redirects=True)
    assert b"Se connecter" in response.data

def test_livre_delete_after_login(client):
    """Teste que la page de confirmation de suppression s'affiche bien une fois connecté."""
    response = login(client, "CDAL", "AIGRE", "/livres/1/delete/")
    assert response.status_code == 200
    assert b"Supprimer le livre" in response.data