import pytest
from monApp import app, db
from monApp.models import Auteur

@pytest.fixture
def testapp():
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False
    })
    with app.app_context():
        db.create_all()
        # Ajouter un auteur de test
        auteur = Auteur(Nom="Victor Hugo")
        db.session.add(auteur)
        db.session.commit()
        yield app
        # Cleanup après les tests
        db.drop_all()

@pytest.fixture
def client(testapp):
    return testapp.test_client()