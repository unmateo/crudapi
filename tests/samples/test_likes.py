from fastapi.testclient import TestClient

from samples.apps.likes import Likes
from samples.models import Like
from samples.models import Tag


def test_likes():
    app = Likes()
    client = TestClient(app)
    assert app


def test_models(db):
    like = Like(url="TestURL", title="TestTitle", tags=[Tag(tag="TestTag")])
    db.add(like)
    db.commit()
    assert like
