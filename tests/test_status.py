from app import app


def test_api_status():
    client = app.test_client()
    resp = client.get("/api/status")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "ok"
    assert "vivo" in data["message"]
