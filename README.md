### Building and running
```bash
export COMPOSE_FILE=local.yml

docker-compose build
docker-compose up
```

### Rebuild Django Migrations
```bash
docker-compose down
docker volume ls
docker volume rm hrm_local_postgres_data
docker-compose up
```

### Run individual django console
```bash
docker-compose ps
docker rm -f back_django_1
docker-compose run --rm --service-ports django
```
### Create Super User
```bash
docker-compose run --rm django \
    python manage.py createsuperuser
```

### Migrations
```bash
docker-compose run --rm django \
    python manage.py makemigrations

docker-compose run --rm django \
    python manage.py migrate
```
### Tests

```bash
docker-compose run --rm django \
    pytest
```


## Contributors

- [Pablo Trinidad](https://github.com/pablotrinidad)
- [Yerson Lasso](https://github.com/unknowncoder05)
