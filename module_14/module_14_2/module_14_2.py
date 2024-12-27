import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')

# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'ex{i}@gmail.com', i * 10, 1000))
#
# cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 = ?', (500, 1))
#
# cursor.execute('DELETE FROM Users WHERE id % 3 = ?', (1,))

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))


cursor.execute('SELECT COUNT(*) FROM Users')
count_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
sum_balances = cursor.fetchone()[0]
avg_balance = sum_balances / count_users
print(f'Средней баланс всех пользователей: {avg_balance}')


connection.commit()
connection.close()