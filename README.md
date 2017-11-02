How to:
1. Клонируем репозиторий: `git clone https://github.com/NosyParker/test-django.git`
2. Переходим в папку с проектом: `cd test-django`
3. Создаем виртуальное окружение: `python -m venv test-django`
4. Активируем окружение: `source test-django/bin/activate`
5. Устанавливаем необходимые пакеты: `pip install -r requirements.txt`
6. Делаем миграцию БД: `python manage.py migrate`
7. Запускаем: `python manage.py runserver`