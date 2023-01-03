# from http.server import HTTPServer, BaseHTTPRequestHandler


# class Serv(BaseHTTPRequestHandler):

#     def do_GET(self):
#         if self.path == '/':
#             self.path = '/index.html'
#         try:
#             file_to_open = open(self.path[1:]).read()
#             self.send_response(200)
#         except:
#             file_to_open = "File not found"
#             self.send_response(404)
#         self.end_headers()
#         self.wfile.write(bytes(file_to_open, 'utf-8'))


# httpd = HTTPServer(('localhost', 8080), Serv)
# httpd.serve_forever()

import http.server
import socketserver

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(f'Received request for {self.path}')
        try:
            with open('index.html', 'rb') as f:
                html = f.read()
        except Exception as e:
            print(f'Error: {e}')
            self.send_response(500)
            return
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html)

PORT = 8000

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
