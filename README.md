# Django-custom-user

<img height="30em" src="https://raw.githubusercontent.com/anki-geo/ultimate-geography/a44a569a922e1d241517113e2917736af808eed7/src/media/flags/ug-flag-russia.svg" alt="russian" style="display: block; margin-bottom: 1em"/>
Django-приложение для регистрации пользователей по email с подтверждением.

- **Язык**: Русский, Английский
- **Автор**: [Андрей Плеханов](https://t.me/andryplekhanov)

## Особенности и возможности
- расширенная модель пользователя с дополнительными полями
- регистрация пользователей по email и паролю
- отправка письма со ссылкой для подтверждения регистрации
- сброс пароля по email
- личный кабинет пользователя с возможностью редактировать свои данные

### !Важно
Везде, где нужно обратиться к модели **User** (например в **forms** или **views**), нужно:
- прописать импорт `from django.contrib.auth import get_user_model`
- объявить модель так: `User = get_user_model()`
- обращаться к модели привычным способом: `User.objects.get(pk=pk)`

## Установка и запуск
1. Скачать скрипт и распаковать архив
2. Создать и активировать виртуальное окружение
3. Создать в главной директории файл `.env` и прописать необходимые настройки (для примера см. файл `env_template`)
4. Установить зависимости: `pip install -r requirements.txt`
5. Применить миграции: `python manage.py migrate`
6. Создать суперпользователя: `python manage.py createsuperuser`
7. Запустить сервер: `python manage.py runserver`
8. Перейти по адресу: http://127.0.0.1:8000/

<hr>
<img height="30em" src="https://raw.githubusercontent.com/anki-geo/ultimate-geography/a44a569a922e1d241517113e2917736af808eed7/src/media/flags/ug-flag-united_kingdom.svg" alt="english" style="display: block; margin-bottom: 1em"/>
Django-application for registering users by email with confirmation.

- **Language**: Russian, English
- **Author**: [Andrey Plekhanov](https://t.me/andryplekhanov)

## Features and capabilities
- extended user model with additional fields
- signing up by email and password
- sends an email with a link to confirm registration
- reset password by email
- user's personal account with the option to edit personal data

### !Important
Wherever you need to refer to the **User** model (for example in **forms** or **views**), you should:
- register import `from django.contrib.auth import get_user_model`
- declare the model like this: `User = get_user_model()`
- refer to the model in the usual way: `User.objects.get(pk=pk)`

## Installation and launch
1. Download the scripts and unpack the archive
2. Create and activate a virtual environment
3. Create in the main directory `.env`-file and register the necessary settings (as an example, `env_template`)
4. Install dependencies: `pip install -r requirements.txt`
5. Apply Migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`
8. Go to: http://127.0.0.1:8000/
