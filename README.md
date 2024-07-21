1. Для запуска потребуется установить библиотеки из requirements.txt

pip install -r requirements.txt


2. Создать файл с зависимостями (.env) и заполнить по поля из .env.default

BOT_TOKEN=токен_бота

REDIS_PASSWORD=пароль_от_редиски
REDIS_USER=пользователь
REDIS_USER_PASSWORD=пароль_пользователя

REDIS_HOST=хост_где_крутится_редиска(если для запуска docker-compose то называем именем сервиса из docker-compose.yml)
REDIS_PORT=порт_где_крутится_редиска
REDIS_DB=бд_редиски

PRICES_CB=ссылка_данные_с_курсами_валют

3.Запускаем docker-compose

docker-compose up --build


ГОТОВО
