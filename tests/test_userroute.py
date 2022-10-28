from fastapi.testclient import TestClient
import json
from main import app


client = TestClient(app)
 
def test_user():
    data = {"username":"testuser8","email":"testuser8@gmail.com","password":"testing123","is_superuser":False}
    response = client.post("/user", json.dumps(data))
    assert response.status_code == 201
    assert response.json()['username'] == "testuser8"