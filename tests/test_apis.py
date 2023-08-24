from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Hello World"}


def test_get_sys_info():
    response = client.get("/system/states")
    assert response.status_code == 200
    assert response.json() == {
        "available_states": ['Standby (S3)', 'Hibernate', 'Hybrid Sleep', 'Fast Startup'],
        "error": False,
        "error_message": None
    }

