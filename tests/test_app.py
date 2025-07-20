import unittest
import os
os.environ["TESTING"] = "true"

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow Portfolios</title>" in html
        assert "<h1>MLH Fellow Portfolios</h1>" in html
        assert "Lucas" in html
        assert "Stephany" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_post" in json
        assert len(json["timeline_post"]) == 0

    def test_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": "Hello, world!"})
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "id" in json
        assert json["name"] == "John Doe"
        assert json["email"] == "john@example.com"
        assert json["content"] == "Hello, world!"
    
    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        print(html)
        assert "Invalid name" in html

        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
