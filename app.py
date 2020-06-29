# https://tinydb.readthedocs.io/en/stable/getting-started.html

from tinydb import TinyDB, Query

db = TinyDB('db.json')

# db.insert({'Food': 'Tacos', 'count': 4})
db.insert({'Food': 'Cookies', 'count': 5})
db.insert({'Food': 'Donuts', 'count': 15})
db.insert({'Food': 'Eggs', 'count': 8})