FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y cron vim

RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

#CMD ["gunicorn", "-c", "config/gunicorn/config.py", "--bind", ":8000", "--chdir", "docker_django", "docker_django.wsgi:application"]

#RUN python docker_django/manage.py makemigrations
#RUN python docker_django/manage.py migrate

#RUN python docker_django/manage.py createsuperuser

RUN service cron start
RUN python docker_django/manage.py crontab add
RUN python docker_django/manage.py crontab show
RUN service cron restart

#COPY example-crontab /etc/cron.d/example-crontab

#RUN chmod 0644 /etc/cron.d/example-crontab && crontab /etc/cron.d/example-crontab