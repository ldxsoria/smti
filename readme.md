# SIGMA MIT
Es una aplicación desarrollada en Django, que utiliza las siguientes tecnologías:
* Docker y Docker-compose
* Git
* Python ,gunicorn y el framework Django
* Nginx
* Postgresql

# Primero clonamos el projecto
```bash
git clone https://github.com/ldxsoria/sigma-mti.git
```

# Creamos los contenedores y los inicializamos
```bash
cd sigma-mti
docker-compose up -d
```

# Configuramos django
```bash
docker-compose exec django_app python docker_django/manage.py makemigrations
docker-compose exec django_app python docker_django/manage.py migrate
docker-compose exec django_app python docker_django/manage.py collectstatic
```
# Configuramos el superusuario de django
```bash
docker-compose exec django_app python docker_django/manage.py createsuperuser
```

# Una vez echo todo lo anterior, realizamos lo siguiente:
1) Ingresamos al {{dominio}}/admin con la cuenta de superusuario
2) Ingresamos a {{dominio}}/ y importamos lo siguiente desde un .csv:
* Estados de los tickets de atención => (int:estado, str:desc)
* Usuarios => (username,first_name,last_name,email,password)
* Areas =>  (str:cod_area, str: descrpition, str:siglas)

# Iniciamos CRONJOBS
```bash
docker-compose exec django_app service cron restart
```
