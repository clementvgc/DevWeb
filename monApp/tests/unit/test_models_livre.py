from monApp.models import Livre

def test_livre_init():
    """ Teste l'initialisation d'un Livre. """
    livre = Livre(Titre="Le Dernier Jour d'un Condamné", Prix=5.99, Url="http://example.com", Img="image.jpg", auteur_id=1)
    assert livre.Titre == "Le Dernier Jour d'un Condamné"
    assert livre.Prix == 5.99

def test_livre_repr(testapp):
    """ Teste la représentation textuelle d'un Livre. """
    with testapp.app_context():
        livre = Livre.query.get(1)
        assert repr(livre) == "<Livre (1) Les Misérables>"