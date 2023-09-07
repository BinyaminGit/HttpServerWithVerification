import unittest
import requests
import threading
import json
from http_server import run_server

"""
setUpClass Method: Initializes the server in a separate daemon thread to ensure it runs independently of the test suite.

Test Methods: Contains various unit tests to verify the server's functionality, including response codes, response content, and POST/GET methods on /data.

Performance Test: A basic performance test that sends 100 GET requests to the server to ensure it can handle multiple requests quickly.
"""
class TestHTTPServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(target=run_server)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    def test_server_response_code(self):
        response = requests.get('http://localhost:8000')
        self.assertEqual(response.status_code, 200)

    def test_server_response_content(self):
        response = requests.get('http://localhost:8000')
        self.assertEqual(response.text, 'Hello, Example SDK!')

    def test_data_route_post(self):
        response = requests.post('http://localhost:8000/data', json={'key': 'value'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'status': 'success'})

    def test_data_route_get(self):
        requests.post('http://localhost:8000/data', json={'key': 'value'})
        response = requests.get('http://localhost:8000/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'value'})

    def test_server_performance(self):
        for i in range(100):
            response = requests.get('http://localhost:8000')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
