from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

"""
Imports and Class Definition: It imports the necessary modules and defines a handler class that inherits from SimpleHTTPRequestHandler.

Data Store: A class-level dictionary data_store is created to simulate a small data storage.

do_GET Method: Defines what to do when a GET request is received. It has two routes:

/data: Returns a JSON object representing the data_store.
do_POST Method: Defines what to do when a POST request is made to /data. It updates data_store with the data received.

run_server Function: This function initializes the server on port 8000 and makes it ready to serve requests indefinitely.
"""
class MyHandler(SimpleHTTPRequestHandler):
    data_store = {}

    def do_GET(self):
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self.data_store).encode())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, Example!')

    def do_POST(self):
        if self.path == '/data':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            self.data_store.update(data)

            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'success'}).encode())

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print('HTTP server running on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
