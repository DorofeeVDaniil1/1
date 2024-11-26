import requests

# URL API для получения постов
url = "https://jsonplaceholder.typicode.com/posts"

# Отправка GET-запроса
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    # Преобразование данных в JSON
    posts = response.json()
    print("Список постов успешно получен!")
    print(f"Пример данных (первые 2 записи): {posts[:2]}")
else:
    print(f"Ошибка при выполнении запроса: {response.status_code}")

#C:\Users\dandy\PycharmProjects\SQLite\.venv\Scripts\python.exe C:\Users\dandy\PycharmProjects\SQLite\Task2.py
#Список постов успешно получен!
# данных (первые 2 записи): [{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}, {'userId': 1, 'id': 2, 'title': 'qui est esse', 'body': 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'}]

#Process finished with exit code 0
#
#
#
#