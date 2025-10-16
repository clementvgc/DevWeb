from .test_routes_auteur import login

def test_index_page(client, testapp):
    response = client.get('/')
    assert response.status_code == 200

def test_about_page(client, testapp):
    response = client.get('/about/')
    assert response.status_code == 200
    assert b"Page \xc3\x80 propos" in response.data  
    assert b"Ce site est un test pour un tp" in response.data

def test_contact_page(client, testapp):
    response = client.get('/contact/')
    assert response.status_code == 200
    assert b"Page de contact" in response.data
    assert b"07 23 34 31 28" in response.data

def test_logout(client, testapp):
    login(client, "CDAL", "AIGRE", "/")

    response = client.get('/logout/', follow_redirects=True)
    assert response.status_code == 200

    assert b"Vous \xc3\xaates connect\xc3\xa9" not in response.data 

    response_protected = client.get('/auteur/', follow_redirects=True)
    assert b"Se connecter" in response_protected.data