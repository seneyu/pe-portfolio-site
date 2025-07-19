import unittest
from peewee import *
from app import app, TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for test
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # build model classes to test db
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)
        self.client = app.test_client()

    def tearDown(self):
        # not strictlyl necessary since SQList in-memory databases only live for duration of connection
        test_db.drop_tables(MODELS)
        
        test_db.close()

    def test_timeline_post(self):
        # add data to db 
        first_post = TimelinePost.create(name='John Doe', email='john@email.com', content='Hello I am John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@email.com', content='Hello I am Jane!')
        assert second_post.id == 2

        # fetch response via API
        get_response = self.client.get("/api/timeline_post")
        self.assertEqual(get_response.status_code, 200)
        data = get_response.get_json()
        self.assertIn("timeline_posts", data)
        posts = data["timeline_posts"]

        self.assertEqual(posts[0]["name"], "Jane Doe")
        self.assertEqual(posts[1]["name"], "John Doe")

        # delete posts
        delete_response1 = self.client.delete("/api/timeline_post", data={"id": second_post.id})
        self.assertEqual(delete_response1.status_code, 200)
        delete_response2 = self.client.delete("/api/timeline_post", data={"id": first_post.id})
        self.assertEqual(delete_response2.status_code, 200)

        # confirm there are no posts left
        get_response = self.client.get("/api/timeline_post")
        data = get_response.get_json()
        posts = data["timeline_posts"]
        self.assertEqual(len(posts), 0)