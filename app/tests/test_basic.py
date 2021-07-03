
import unittest

from app import create_app, db

app = create_app()
app.app_context().push()


class BasicTests(unittest.TestCase):

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

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_can_404_gracefully(self):
        response = self.app.get('/thispagedoesnotexist', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        assert b'The page you requested does not exist' in response.data


    def test_api_info(self):
        response = self.app.get('/api', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert b'API Info' in response.data






if __name__ == "__main__":
    unittest.main()



