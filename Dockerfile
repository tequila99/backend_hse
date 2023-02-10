FROM python:3.10-slim

WORKDIR /home/app

COPY ./requirements.txt ./requirements.txt

RUN  pip config set global.trusted-host 'files.pythonhosted.org pypi.org'
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

ENTRYPOINT python manage.py migrate && \
#           python manage.py collectstatic --no-input && \
           gunicorn -b 0.0.0.0:8000 \
                --preload \
                --workers 4 \
                --log-level INFO \
                --graceful-timeout 60 \
                --timeout 360 todo.wsgi:application
