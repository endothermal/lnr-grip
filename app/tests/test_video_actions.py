
import unittest
import json

from app.tests.test_basic import app, db


class VideoActionsTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

        self.app = app.test_client()
        db.create_all()

        # Disable sending emails during unit testing
        # mail.init_app(app)
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    ###############
    #### tests ####
    ###############


    def test_api_video_actions(self):
        response = self.app.get('/api/v1.0/video_actions', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert len(response.get_json())==7

    def test_api_video_actions_action_stop(self):
        response = self.app.get('/api/v1.0/video_actions?action=stop', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert len(response.get_json())==3
        assert b'"action":"stop"' in response.data
        assert b'"action":"start"' not in response.data

    def test_api_video_actions_action_start(self):
        response = self.app.get('/api/v1.0/video_actions?action=start', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert len(response.get_json())==4
        assert b'"action":"start"' in response.data
        assert b'"action":"stop"' not in response.data

    def test_api_video_actions_action_any(self):
        response = self.app.get('/api/v1.0/video_actions?action=balderdash', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert len(response.get_json())==7

    def test_api_video_actions_start_time(self):
        response = self.app.get('/api/v1.0/video_actions?start_time=0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert len(response.get_json())==7
        response = self.app.get('/api/v1.0/video_actions?start_time=700', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert len(response.get_json()) == 1

    def test_api_video_actions_bad_start_time(self):
        response = self.app.get('/api/v1.0/video_actions?start_time=rubbish', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert len(response.get_json())==7

    def test_api_video_actions_end_time(self):
        response = self.app.get('/api/v1.0/video_actions?end_time=0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert len(response.get_json())==0
        response = self.app.get('/api/v1.0/video_actions?end_time=700', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert len(response.get_json()) == 6

    def test_api_video_actions_bad_end_time(self):
        response = self.app.get('/api/v1.0/video_actions?end_time=rubbish', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert len(response.get_json())==7

    def test_api_video_actions_end_time_before_start_time(self):
        response = self.app.get('/api/v1.0/video_actions?end_time=10&start_time=20', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert len(response.get_json())==0

    def test_video_actions(self):
        response = self.app.get('/get_video_actions', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)

    def test_video_actions_with_parameters(self):
        response = self.app.get('/get_video_actions?action=stop&start_time=400&end_time=600', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert b'iPhone 8s' in response.data
        assert b'OSX 15.4' in response.data







