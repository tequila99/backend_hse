### Код с мастер-класса в ВШЭ

### Запуск:
#### Через докер:
`docker-compose up --build`
#### Локальный запуск:
##### Нужно сделать в первый раз:
`python -m venv venv`

On Unix or Linux: `source venv/bin/activate` On Windows:`venv\Scripts\activate.bat`

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py createsuperuser`

##### Далее:
`python manage.py runserver`

### Полезные ссылки:
https://docs.djangoproject.com/en/4.1/intro/tutorial01/

https://www.django-rest-framework.org/tutorial/1-serialization/

https://docs.djangoproject.com/en/4.1/ref/models/fields/#choices

https://t.me/pydjango

https://t.me/django_jobs_board
