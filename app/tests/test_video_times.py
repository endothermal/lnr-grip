
import unittest
import json

from app.tests.test_basic import app, db


class VideoTimesTests(unittest.TestCase):

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


    def test_api_video_times(self):
        response = self.app.get('/api/v1.0/video_times', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert len(response.get_json())==3
        assert b'total_duration' in response.data

    def test_api_video_times_1(self):
        response = self.app.get('/api/v1.0/video_times/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert b'total_duration' in response.data
        assert b'"user_id":1}' in response.data


    def test_api_video_times_user_does_not_exist(self):
        response = self.app.get('/api/v1.0/video_times/123456789', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        assert b'Could not find user' in response.data

    def test_api_video_times_bad_user_id(self):
        response = self.app.get('/api/v1.0/video_times/string', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_api_video_times_no_user_id(self):
        response = self.app.get('/api/v1.0/video_times/', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_video_times(self):
        response = self.app.get('/get_video_times', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert b'Total duration' in response.data

    def test_video_times_user_id(self):
        response = self.app.get('/get_video_times/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert b'430' in response.data





