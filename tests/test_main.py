from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_company_info():
    response = client.get("/api/company")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "VSpireInnovations"
    assert data["tagline"] == "We Vision Inspiration"


def test_home_page():
    response = client.get("/")

    assert response.status_code == 200
    assert "Shweta Sudhir Sakhare" in response.text