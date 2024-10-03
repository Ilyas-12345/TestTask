# Тестовое задание

## Содержание
- [Инструкция по запуску приложения](#Инструкция-по-запуску-приложения)
- [Документация Swagger](#Документация)
  
# Инструкция по запуску приложения

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/Ilyas-12345/TestTask.git
   cd TestTask
2. Установите зависимости:
   ```
   pip install -r requirements.txt
3. Настройка переменных окружения
   Создайте файл `.env-non-dev` в корневом каталоге и укажите переменные для доступа в бд:
 ```
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password
    POSTGRES_DB=your_db_name
 ```
4. Запустите приложение с помощью Docker Compose:
   ```
   docker-compose up --build 
# Документация

Докумантация представлена в формате **Swagger**





