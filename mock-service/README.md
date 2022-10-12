# Mock сервис по рассылке SMS сообщений

Приложение эмулирует работу сервиса по отправке SMS-сообщений.<br>
Для авторизации используется логин и пароль, а также JWT-токены.
<br>Максимальная длинна SMS сообщения 140 символов, если сообщение длиннее 140 символов оно делится на части.
<br>Сервис может отдавать 500 ошибку в зависимости от настроек.
<br>Логи приложения хранятся в директории logs.

### Основные эндпоиты

`/swagger/` - документация приложения;<br>
`/api/get/status` - получить список сообщений пользователя;<br>
`/api/post/message` - отправить сообщение абоненту;<br>
`/api/rest-auth/login/` - получить токен.<br>

## Docker
Используется несколько docker-compose файлов для разработки и тестирования приложения.

`docker-compose.yaml` - запускает только PostgreSQL в контейнере. Файлы базы данных хранятся вне контейнера.<br>
`docker-compose.dev.yaml` - запускает сервис в режиме разработчика. Запускается база данных и приложение с помощью manage.py.<br>
`docker-compose.prod.yaml` - запускает сервис в production режиме. Для запускается nginx для проксирования запросов. Приложение запускается при помощи gunicorn. Приложение доступно на порту 8001;<br>
`docker-compose run django-mock python manage.py createsuperuser` - создать администратора.

### Команды
`$ docker-compose build -f docker-compose.[|dev|prod]yaml` - команда для сборки образов;<br>
`$ docker-compose -f docker-compose.[|dev|prod]yaml up -d` - команда для запуска образов;<br>
`$ docker-compose exec django-mock python manage.py migrate --noinput` - запуск миграций в контейнере.

## Настройки
В файле env.* можно установить количество возвращаемых ответов с кодом 202 для эндпоинта `/api/post/message`<br>
`PERCENT_OF_GOOD_RESPONSE=100`


## Примеры запросов

Получить токен:<br>
```curl --location --request POST 'http://127.0.0.1:8000/api/rest-auth/login/' \
--header 'Cookie: csrftoken=hbkhmSYuMwsDhRgBoEF0ClVMoPbRboMv; jwt-auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1NjA3MjYzLCJpYXQiOjE2NjU2MDY5NjMsImp0aSI6IjhmMzJiYWNlYzgwYjQzMWQ4MGM3NDc1OWE1NDRhMjcwIiwidXNlcl9pZCI6MX0.Xl1tMe3pdcxngLKuDS8rnibY5zkoJlB3Oy5c9hhLrmY; sessionid=ybsiaxmvne4bvgf5hj67m7wte24jmklc' \
--form 'username="admin"' \
--form 'password="admin"'
```

Посмотреть список сообщений пользователя:<br>
```
curl --location --request GET 'http://127.0.0.1:8000/api/get/status' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1NTI4Nzg5LCJpYXQiOjE2NjU1Mjg0ODksImp0aSI6IjQ4NmMyOTA4ZmJlNDQyY2I5MzhkNzkxYzYxYTIzNDk0IiwidXNlcl9pZCI6MX0.cmBwSIN5RE9qn9Upj0-D9av8qzfDdR67ps7kJxz6Qn8' \
--header 'Cookie: csrftoken=4JEQsjZ2r8S2JlGIXMRqHTv0uwfG4iW0; sessionid=ybsiaxmvne4bvgf5hj67m7wte24jmklc'
```

 Отправить сообщение:<br>
```
curl --location --request POST 'http://127.0.0.1:8000/api/post/message' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1NjExMDAzLCJpYXQiOjE2NjU2MTA3MDMsImp0aSI6ImEyM2EwOTRlYjhhZjQzMmJiYTExNGMwOWI4NjE0YTdmIiwidXNlcl9pZCI6MX0.n2nqnMue1-3OCF8d2g8qN4z6RewX7BSSfITDNtzPXYw' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=9fLfMSYorO5m1vwBG89hnKeujGdCudY3; jwt-auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1NjExMDAzLCJpYXQiOjE2NjU2MTA3MDMsImp0aSI6ImEyM2EwOTRlYjhhZjQzMmJiYTExNGMwOWI4NjE0YTdmIiwidXNlcl9pZCI6MX0.n2nqnMue1-3OCF8d2g8qN4z6RewX7BSSfITDNtzPXYw; sessionid=ybsiaxmvne4bvgf5hj67m7wte24jmklc' \
--data-raw '{
    "phone": "100000000",
    "body": "New message"
}' 
```