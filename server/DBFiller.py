import json
import random

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, justo in finibus aliquet, arcu turpis ultricies lacus, a tincidunt augue nulla nec velit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam euismod, nulla sit amet aliquam convallis, mauris erat blandit nunc, eget elementum ex felis id sapien. Nulla nec lorem vitae ipsum facilisis fringilla. Donec auctor, sem ut semper porttitor, nunc massa finibus dui, id vestibulum lorem nibh non libero. Integer pulvinar turpis vitae nibh euismod, a tincidunt lectus imperdiet. Etiam ut'
title = 'Lorem ipsum'

with open('database.json', 'r', encoding='utf-8') as f:
    database = json.load(f)
    database['articles'] = {
        int(articleID): article for articleID, article in database['articles'].items()}

for i in range(100):
    database['articles'][i] = {
        'title': f'{title} {i}',
        'text': f'{i} {text}',
        'likes': 0
    }

for user in database['users'].values():
    user['likes'] = []

with open('database.json', 'w', encoding='utf-8') as f:
    json.dump(database, f, indent=4)