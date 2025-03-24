# Проверка соединения с huggingface

import requests

def check_huggingface_connection():
    url = "https://huggingface.co"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("Подключение выполнено успешно")
        else:
            print(f"Ошибка: статус-код {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Не удалось подключиться к Haggingface: {e}")

check_huggingface_connection()

# ##########
# ##########

# # Установка модели all-MiniLM-L6-v2, эта модель используется для создания эмбеддингов (векторных представлений числа)
# from sentence_transformers import SentenceTransformer

# # Загрузка модели
# model = SentenceTransformer('all-MiniLM-L6-v2')

# # Сохранение модели в папке проекта
# model.save('./models/all-MiniLM-v2')

# ##########
# ##########

# # Проверка работы модели all-MiniLM-L6-v2 локально
# from sentence_transformers import SentenceTransformer

# # Загрузка модели из локальной папки
# model = SentenceTransformer("./models/all-MiniLM-L6-v2")

# # Пример использования
# embeddings = model.encode("Привет, мир!")
# print(embeddings)