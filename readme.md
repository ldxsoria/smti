docker-compose up --build
docker-compose up -d

docker-compose run django_app python docker_django/manage.py migrate
docker-compose run django_app python docker_django/manage.py createsuperuser
docker-compose run django_app python docker_django/manage.py collectstatic

docker-compose stop django_app
docker-compose start django_app
docker-compose restart django_app

docker-compose exec -it db_postgres /bin/sh