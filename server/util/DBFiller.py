import json
import sys

content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, justo in finibus aliquet, arcu turpis ultricies lacus, a tincidunt augue nulla nec velit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam euismod, nulla sit amet aliquam convallis, mauris erat blandit nunc, eget elementum ex felis id sapien. Nulla nec lorem vitae ipsum facilisis fringilla. Donec auctor, sem ut semper porttitor, nunc massa finibus dui, id vestibulum lorem nibh non libero. Integer pulvinar turpis vitae nibh euismod, a tincidunt lectus imperdiet. Etiam ut'
title = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, justo in'

if len(sys.argv) < 2:
    print('Usage: python DBFiller.py <json_path> <number_of_articles>')
    exit()

database_path = sys.argv[1]
number_of_articles = int(sys.argv[2])

with open(database_path, 'r', encoding='utf-8') as f:
    database = json.load(f)

database['articles'] = {}

for i in range(1, number_of_articles+1):
    database['articles'][i] = {
        'title': f'{title} {i}',
        'content': f'{i} {content}',
        'likes': 0
    }

for user in database['users'].values():
    user['likes'] = []

with open(database_path, 'w', encoding='utf-8') as f:
    json.dump(database, f, indent=4)