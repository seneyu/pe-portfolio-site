import unittest
import os
from app import app, TimelinePost
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        TimelinePost.delete().execute() # clean db for test isolation

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow Portfolios</title>" in html
        # TODO Add more tests relating to the home page
        assert "<h1>MLH Fellow Portfolios</h1>" in html
        assert '<img src="./static/img/logo.jpg"' in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        # TODO Add more tests relating to the timeline page

    def test_post_and_get_timeline_post(self):
        self.client.post("/api/timeline_post", data={"name": "Jane Doe", "email": "jane@email.com", "content": "Test!"})
        response = self.client.get("/api/timeline_post")
        data = response.get_json()
        assert len(data["timeline_posts"]) == 1
    
    def test_delete_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@email.com", "content": "Delete me!"})
        post_id = response.get_json()["id"]
        delete_response = self.client.delete("/api/timeline_post", data = {"id": post_id})
        assert delete_response.status_code == 200
        check = self.client.get("/api/timeline_post").get_json()
        assert all(p["id"] != post_id for p in check["timeline_posts"])

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I am John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I am John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html