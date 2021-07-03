
import unittest
import json

from app.tests.test_basic import app, db


class APITests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
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


    def test_api_users(self):
        response = self.app.get('/api/v1.0/users', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert b'first_name' in response.data

    def test_api_user_1(self):
        response = self.app.get('/api/v1.0/users/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert b'first_name' in response.data

    def test_api_user_does_not_exist(self):
        response = self.app.get('/api/v1.0/users/123456789', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        assert isinstance(response.data, object)
        assert b'Could not find user' in response.data

    def test_api_bad_user_id(self):
        response = self.app.get('/api/v1.0/users/string', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        assert isinstance(response.data, object)
        assert b'The page you requested does not exist' in response.data

    def test_api_no_user_id(self):
        response = self.app.get('/api/v1.0/users/', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        assert isinstance(response.data, object)
        assert b'The page you requested does not exist' in response.data




