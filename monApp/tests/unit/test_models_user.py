from monApp.models import User, load_user

def test_user_get_id():
    """ Teste la méthode get_id de l'User. """
    user = User(Login="test", Password="password_hash")
    assert user.get_id() == "test"

def test_load_user(testapp):
    """ Teste la fonction load_user. """
    with testapp.app_context():
        user = load_user("CDAL")
        assert user.Login == "CDAL"