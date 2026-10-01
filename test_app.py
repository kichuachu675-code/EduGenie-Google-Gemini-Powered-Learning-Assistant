from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_home():
    r = client.get("/")
    assert r.status_code == 200
    assert "EduGenie" in r.text
def test_learn():
    r = client.post("/learn", data={"topic":"Python","level":"Beginner","mode":"Explanation"})
    assert r.status_code == 200
    assert "Python" in r.text
