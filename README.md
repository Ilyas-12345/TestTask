# Тестовое задание

## Содержание
- [Инструкция по запуску приложения](#Инструкция-по-запуску-приложения)
- [Документация Swagger](#Документация)
  
# Инструкция по запуску приложения

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/Ilyas-12345/TestTask.git
   cd TestTask
   ```
   
2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
   
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
   ```

   Приложение будет доступно по адресу [http://localhost:9999](http://localhost:9999)
   
# Документация

Докумантация представлена в формате **Swagger**. Документаци доступна по ссылке - [http://localhost:9999/docs](http://localhost:9999/docs)

Ниже представлен скрин **Swagger**
![Swagger](https://github.com/user-attachments/assets/cfb3e63d-cb79-43b2-9f6b-fae1bb5da627)







