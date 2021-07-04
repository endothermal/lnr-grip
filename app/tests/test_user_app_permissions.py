
import unittest
import json

from app.tests.test_basic import app, db


class UserAppPermisssionsTests(unittest.TestCase):

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


    def test_api_user_app_permissions(self):
        response = self.app.get('/api/v1.0/user_app_permissions', follow_redirects=True)
        self.assertEqual(response.status_code, 404)


    def test_api_user_app_permissions_1(self):
        response = self.app.get('/api/v1.0/user_app_permissions/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert isinstance(response.data, object)
        assert b'application_permissions' in response.data
        assert b'app_id":1,"features_allowed":[1,2]' in response.data


    def test_api_user_app_permissions_user_does_not_exist(self):
        response = self.app.get('/api/v1.0/user_app_permissions/123456789', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        assert b'Could not find user' in response.data

    def test_api_user_app_permissions_bad_user_id(self):
        response = self.app.get('/api/v1.0/user_app_permissions/string', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_user_app_permissions_api_no_user_id(self):
        response = self.app.get('/api/v1.0/user_app_permissions/', follow_redirects=True)
        self.assertEqual(response.status_code, 404)







