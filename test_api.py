import pytest

try:
    from app import app
except ImportError:
    app = None


@pytest.mark.skipif(app is None, reason="Connect this test to the project's Flask app")
def test_get_vehicles_api():
    client = app.test_client()
    response = client.get("/api/vehicles")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
