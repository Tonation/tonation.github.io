import os
from http.server import HTTPServer, CGIHTTPRequestHandler

# Make sure the server is created at current directory
os.chdir('.')

# Create server object listening the port 80
server_object = HTTPServer(server_address=('', 7000), RequestHandlerClass=CGIHTTPRequestHandler)

# Start the web server

print('Server is listening on port 7000')
server_object.serve_forever()