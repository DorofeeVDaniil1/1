import sqlite3
import requests

# URL API для получения постов
url = "https://jsonplaceholder.typicode.com/posts"

# Отправка GET-запроса
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()  # Преобразуем JSON-ответ в Python-объект

    # Подключение к базе данных SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Вставка данных в таблицу posts
    for post in posts:
        cursor.execute('''
        INSERT OR IGNORE INTO posts (id, user_id, title, body)
        VALUES (?, ?, ?, ?)
        ''', (post['id'], post['userId'], post['title'], post['body']))

    # Подтверждение изменений и закрытие подключения
    conn.commit()
    conn.close()

    print("Данные успешно сохранены в таблицу posts!")
else:
    print(f"Ошибка при выполнении запроса: {response.status_code}")
