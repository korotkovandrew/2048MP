# how to import file from directory ../client/ClientSocket/Sender.py ?
# a:

from ..client.src.ClientSocket.Sender import Sender

NUMBER_OF_USERS = 1000
NUMBER_OF_LIKED_ARTICLES = 10

def generateUsers():
    users = []
    for i in range(100):
        users.append(User(i, f'User{i}'))
    return users


if __name__ == '__main__':
    clientImitation = Sender()
    
    users = generateUsers()