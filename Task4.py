import sqlite3

def get_posts_by_user(user_id):
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # SQL-запрос для получения постов конкретного пользователя
    cursor.execute('''
    SELECT id, user_id, title, body 
    FROM posts
    WHERE user_id = ?
    ''', (user_id,))  # Передача user_id как параметра

    # Извлечение данных
    posts = cursor.fetchall()

    # Закрытие подключения
    conn.close()

    return posts

# Пример использования
user_id = 1  # Укажите идентификатор пользователя
posts = get_posts_by_user(user_id)

if posts:
    print(f"Посты пользователя с ID {user_id}:")
    for post in posts:
        print(f"ID: {post[0]}, Title: {post[2]}")
else:
    print(f"Нет постов для пользователя с ID {user_id}.")
