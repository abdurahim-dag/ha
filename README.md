# Создание и просмотр анкет в социальной сети.

Функциональные требования:
- Простейшая авторизация пользователя.
- Возможность создания пользователя, где указывается следующая информация:
    - Имя
    - Фамилия
    - Возраст
    - Пол
    - Интересы
    - Город
    - Страницы с анкетой.

Нефункциональные требования:
- Любой язык программирования
- В качестве базы данных использовать MySQL (при остром желании PostgreSQL/MariaDB, но стоит иметь ввиду, что по этим базам может не быть возможности задать вопрос преподавателю)
- Не использовать ORM
- Программа должна представлять из себя монолитное приложение.
- Не рекомендуется использовать следующие технологии:
    - Репликация
    - Шардинг
    - Индексы
    - Кэширование

## Решение
API на DRF.

Запуск:
```
docker compose --env-file .\env.example up -d --no-deps --build
```

Для проверки, можно воспользоваться этой спецификацией:
- /login
- /user/register
- /user/get/{id}

Postman-коллекция, для проверки: `HA-Collection.postman_collection.json`.
