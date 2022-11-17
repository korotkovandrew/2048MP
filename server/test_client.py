import socket

HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 2020  # Port to listen on (non-privileged ports are > 1023)

DATA_CLOSING_SEQ = "\r\n\r\n"

ENCODING = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.close()