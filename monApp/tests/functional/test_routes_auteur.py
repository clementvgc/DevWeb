from monApp.app import app

def test_auteurs_liste(client, testapp):
    response = client.get('/auteurs/')
    assert response.status_code == 200
    assert b'Victor Hugo' in response.data

def test_auteur_update_before_login(client, testapp):
    response = client.get('/auteurs/1/update/', follow_redirects=True)
    assert b"Se connecter" in response.data

def login(client, username, password, next_path):
    return client.post( "/login/",
                            data={"Login": username,"Password": password, "next":next_path},
                            follow_redirects=True)
def test_auteur_update_after_login(client,testapp):
    with testapp.app_context():
        response=client.get('/auteurs/1/update/', follow_redirects=False)
        assert response.status_code == 302
        assert "/login/?next=%2Fauteurs%2F1%2Fupdate%2F" in response.headers["Location"]
        response=login(client, "CDAL", "AIGRE", "/auteurs/1/update/")
        assert response.status_code == 200
        assert b"Modification de l'auteur Victor Hugo" in response.data

def test_auteur_view(client, testapp):
    response = client.get('/auteurs/1/view/')
    assert response.status_code == 200
    assert b"Consultation de l'auteur Victor Hugo" in response.data

def test_auteur_delete_before_login(client, testapp):
    response = client.get('/auteurs/1/delete/', follow_redirects=True)
    assert b"Se connecter" in response.data

def test_auteur_delete_after_login(client, testapp):
    response = login(client, "CDAL", "AIGRE", "/auteurs/1/delete/")
    
    assert response.status_code == 200
    assert b"Suppression de l'auteur Victor Hugo. Etes vous sur ?" in response.data

def test_auteur_create_before_login(client, testapp):
    response = client.get('/auteur/', follow_redirects=True)
    assert b"Se connecter" in response.data

def test_auteur_create_after_login(client, testapp):
    response = login(client, "CDAL", "AIGRE", "/auteur/")
    
    assert response.status_code == 200
    assert b"Cr\xc3\xa9ation d'un auteur" in response.data