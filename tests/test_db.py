import os
import unittest
from peewee import *

# Set testing environment before importing app
os.environ['USING_TEST_DB'] = 'true'

from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests
test_db = SqliteDatabase(":memory:")

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name="John Doe", email="john@example.com", content="Hello, world, I'm John!")
        assert first_post.id == 1
        second_post = TimelinePost.create(name="Jane Doe", email="jane@example.com", content="Hello, world, I'm Jane!")
        assert second_post.id == 2

        posts = TimelinePost.select().order_by(TimelinePost.id)
        assert len(posts) == 2
        assert posts[0].name == "John Doe"
        assert posts[1].name == "Jane Doe"

        first_post = TimelinePost.get(TimelinePost.id == 1)
        assert first_post.name == "John Doe"
        assert first_post.email == "john@example.com"

        second_post = TimelinePost.get(TimelinePost.id == 2)
        assert second_post.name == "Jane Doe"
        assert second_post.email == "jane@example.com"
        
