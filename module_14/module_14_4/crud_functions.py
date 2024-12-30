import sqlite3
from pprint import pprint

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL,
img TEXT
)
''')

connection.commit()
connection.close()

# list_products = [
#     {
#         'title': 'Гидролизат коллагена',
#         'description': 'Усиленная формула с эластином, 1 кг',
#         'price': 2500,
#         'img': 'https://cdn.orteka.ru//upload/resize_cache/iblock/901/1200_1200_1d8f616e6dafd84ca6b85089cc850afe3/l18eywjremq294be2by9zesfvlavrzx8.png'
#     },
#     {
#         'title': 'VIPROACTIVE Ven Pro',
#         'description': 'Витамины для здоровья сосудов и вен, капс. 60 шт.',
#         'price': 3000,
#         'img': 'https://cdn.orteka.ru//upload/resize_cache/iblock/b3b/624_624_1d8f616e6dafd84ca6b85089cc850afe3/fydcv6cis3i6hybmkjnqf98e8t0zwisu.jpg'
#     },
#     {
#         'title': 'Натуральный комплекс "Здоровые вены"',
#         'description': 'содержит диосмин и комплекс цитрусовых биофлаваноидов, 60 капсул',
#         'price': 1500,
#         'img': 'https://cdn.orteka.ru//upload/resize_cache/iblock/bf2/1200_1200_1d8f616e6dafd84ca6b85089cc850afe3/1jbg0e6qxcer439j6t35j1dm73io30mv.jpg'
#     },
#     {
#         'title': 'БАД Навимесо Коллаген Джойнтс',
#         'description': '(Navimeso Collagen Joints)',
#         'price': 3500,
#         'img': 'https://cdn.orteka.ru//upload/resize_cache/iblock/ef0/624_624_1d8f616e6dafd84ca6b85089cc850afe3/fnscmtxue3udfvlp6w7o6i1z6vhbjm4e.jpg'
#     },
#
# ]

# for product in list_products:
#     cursor.execute('INSERT INTO Products (title, description, price, img) VALUES (?, ?, ?, ?)',
#                    (product['title'], product['description'], product['price'], product['img']))

async def get_all_products():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Products')
        products = cursor.fetchall()
    return products




