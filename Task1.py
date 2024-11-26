import sqlite3

# Подключение к базе данных SQLite (если файла базы данных нет, он будет создан)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создание таблицы posts
cursor.execute('''
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT,
    body TEXT
)
''')

# Подтверждение изменений и закрытие подключения
conn.commit()
conn.close()

print("База данных и таблица успешно созданы!")
