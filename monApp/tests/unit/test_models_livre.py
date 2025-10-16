from monApp.models import Livre, Auteur

def test_livre_init():
    """ Teste l'initialisation d'un Livre. """
    auteur_test = Auteur(Nom="Test Author")
    livre = Livre(Titre="Le Dernier Jour d'un Condamné", Prix=5.99, Url="http://example.com", Img="image.jpg", auteur=auteur_test)
    assert livre.Titre == "Le Dernier Jour d'un Condamné"
    assert livre.Prix == 5.99

def test_livre_repr(testapp):
    """ Teste la représentation textuelle d'un Livre. """
    with testapp.app_context():
        livre = Livre.query.get(1)
        assert repr(livre) == "<Livre (1) Les Misérables>"