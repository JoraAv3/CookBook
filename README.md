# CookBook

# Django Cookbook

Это приложение представляет собой поварскую книгу на Django с базой данных для хранения продуктов и рецептов.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/JoraAv3/CookBook.git
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd CookBook
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Примените миграции:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Запуск приложения

Выполните следующую команду:

```bash
python manage.py runserver


Использование API

Добавление продукта к рецепту:
curl "http://127.0.0.1:8000/add_product_to_recipe?recipe_id=<recipe_id>&product_id=<product_id>&weight=<weight>"

Приготовление рецепта:
curl "http://127.0.0.1:8000/cook_recipe?recipe_id=<recipe_id>"

Показать рецепты без продукта:
curl "http://127.0.0.1:8000/show_recipes_without_product?product_id=<product_i](http://127.0.0.1:8000/show_recipes_without_product?product_id=<product_id>"


Управление через админку

Запускайте сервер разработки:
python manage.py createsuperuser
python manage.py runserver

Перейдите по адресу http://127.0.0.1:8000/admin/ в вашем браузере.

Войдите с использованием учетных данных администратора.

Управляйте продуктами и рецептами через админку Django.


Это обновленное описание включает в себя упоминание использования базы данных PostgreSQL в инструкции по установке. Пожалуйста, замените `<recipe_id>`, `<product_id>`, `<weight>` и `<product_id>` на реальные значения при использовании API.
