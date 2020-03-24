# D02_sentry_bottle_heroku
Deploying simple bottle web server to heroku. #Sentry.io, #bottle, #heroku, #webr-esponses

Необходимо написать простой веб-сервер с помощью фреймворка Bottle. Все ошибки приложения должны попадать в вашу информационную панель Sentry. Приложение должно размещаться на Heroku, иметь минимум два маршрута:

- /success, который должен возвращать как минимум HTTP ответ со статусом 200 OK
- /fail, который должен возвращать "ошибку сервера" (на стороне Bottle это может быть просто RuntimeError), то есть HTTP ответ со статусом 500
