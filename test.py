import unittest
import FlaskBase


class IndexTestCase(unittest.TestCase):

    def setUp(self):
        FlaskBase.app.config['TESTING'] = True
        self.app = FlaskBase.app.test_client()

    def tearDown(self):
        pass

    def test_index_route_exists(self):
        response = self.app.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Hello, World!")

if __name__ == '__main__':
    unittest.main()
