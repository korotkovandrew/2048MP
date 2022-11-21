# threading multiclient server based on socketserver module

import socketserver

from RequestHandler import RequestHandler

HOST, PORT = "localhost", 2020

# Create the server, binding to localhost on port 2020
with socketserver.TCPServer((HOST, PORT), RequestHandler) as server:
    print(f'Server started at {HOST}:{PORT}')
    server.serve_forever()