import sqlite3
from random import randint

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# cursor.execute(' INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'ex@gmail.com', '28'))

# for i in range(30):
#     cursor.execute(' INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', (f'newuser{i}', 'ex@gmail.com', f'{28 + i}'))

# cursor.execute('UPDATE Users SET age = ? WHERE username = ?', ('29', 'newuser'))

# cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser', ))

# for i in range(30):
#     cursor.execute(' INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', (f'newuser{i}', f'ex{i}@gmail.com', f'{randint(20, 45)}'))

# cursor.execute('SELECT * FROM Users')

# cursor.execute('SELECT username, age FROM Users WHERE age >= ?', (30, ))

# cursor.execute('SELECT username, age FROM Users GROUP BY age')

# users = cursor.fetchall()
# for user in users:
#     print (user)
#


cursor.execute('SELECT COUNT(*) FROM Users')
total1 = cursor.fetchone()[0]
print(total1)
cursor.execute('SELECT SUM(age) FROM Users')
total2 = cursor.fetchone()[0]
print(total2, total2/total1)
cursor.execute('SELECT AVG(age) FROM Users')
total3 = cursor.fetchone()[0]
print(total3)
cursor.execute('SELECT MIN(age) FROM Users')
total4 = cursor.fetchone()[0]
print(total4)
cursor.execute('SELECT MAX(age) FROM Users')
total5 = cursor.fetchone()[0]
print(total5)



connection.commit()
connection.close()

# for SELECT: - выбрать
# FROM - из
# WHERE - где
# GROUP BY - сортировать и группировать без по уникальным значениям
# ORDER BY - сортировать все значения
# HAVING

# COUNT - количество
# SUM - сумма
# AVG - среднее значение
# MIN - минимальное значение
# MAX - максимальное значение