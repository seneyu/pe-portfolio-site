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

        # TODO get timeline posts and assert that they are correct
        posts = list(TimelinePost.select().order_by(TimelinePost.created_at.desc()))
        assert posts[0].name == "Jane Doe"
        assert posts[1].name == "John Doe"