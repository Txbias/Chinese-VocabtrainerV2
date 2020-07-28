import unittest
from app import create_app


class Test(unittest.TestCase):
    def setUp(self) -> None:
        app = create_app()
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self) -> None:
        pass

    def test_root(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_learn(self):
        response = self.app.get('learn', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
