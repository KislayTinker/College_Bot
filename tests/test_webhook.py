import json
from app import app

def test_webhook_known_question():
    client = app.test_client()
    data = {
        "message": {
            "chat": {"id": 12345},
            "text": "What is your name?"
        }
    }
    response = client.post("/webhook", 
                           data=json.dumps(data), 
                           content_type="application/json")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"

def test_webhook_empty_message():
    client = app.test_client()
    data = {"message": {"chat": {"id": 12345}}}
    response = client.post("/webhook", 
                           data=json.dumps(data), 
                           content_type="application/json")
    assert response.status_code == 200
