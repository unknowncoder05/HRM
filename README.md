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



## Contributing

I'll be happily accepting pull requests from anyone, and if you are a
Platzi student **I HIGHLY ENCOURAGE YOU TO CONTRIBUTE!**

This that are missing right now:

* [ ] Add tests and coverage implementations
* [ ] Remove weak Token Authorization system
* [ ] Implement more async and periodic tasks to improve the rating system
* [ ] A UI!

Suggestions are welcome!

If this project get enough attention and participation, I'll be happy
to host it (the UI is required.)

## Want to use this project as yours?

Please stick to the [**LICENSE**](LICENSE), you can read a TL;DR
[here](https://tldrlegal.com/license/mit-license).

Again, this is a project I liked a lot and I will love to see it live
again. Feel free to modify, distribute, use privately, etc (READ THE [**LICENSE**](LICENSE)) as
you please just include the Copyright and the [**LICENSE**](LICENSE).

## Contributors

- [Pablo Trinidad](https://github.com/pablotrinidad)
