# testz
Создание образа
docker build -t app .

Запуск контейнера 
docker run -d -p 8080:5000 app

Для проверки выполнения условия- Сервис должен обрабатывать > 350 запросов в секунду. Нужно запустить локально скрипт test.py

Логи пишутся в файл logs.log. их можно посмотреть зайдя в контейнер с помощью команды
docker exec -ti container id /bin/sh

и открыть файл
cat logs.log

ответ на запрос /reverte
запрос с помощью библиотеки httpie http http://localhost:8080/revert text=asd
или curl
curl -H "Content-Type: application/json" -X POST http://localhost:8080/revert -d "{\"text\":\"Test Value\"}"
ответ
HTTP/1.0 201 CREATED
Content-Length: 19
Content-Type: application/json
Date: Fri, 06 Dec 2019 12:36:59 GMT
Server: Werkzeug/0.16.0 Python/3.7.4

{
    "response": "dsa"
}

2 задание в файле testz2.py
