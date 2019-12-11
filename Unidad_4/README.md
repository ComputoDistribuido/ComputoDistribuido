# Image suppresion project

To start the containerization of our application we'll need to create three containers, one for our django app another for our postgres databse and a third one for our redis message broker server thtat will be hosted on a production server.      

To start head to your django root dir in thise path will locate our Dockerfile that we'll need to build our image for the django app container

Our django proyect folder structure should look like this:

```bash
django-app
   ├── db.sqlite3
   ├── Dockerfile
   ├── image_parroter
   │   ├── celery.py
   │   ├── __init__.py
   │   ├── __pycache__
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── manage.py
   ├── media/
   ├── requirements.txt
   └── thumbnailer
       ├── admin.py
       ├── apps.py
       ├── __init__.py
       ├── migrations
       │   ├── __init__.py
       │   └── __pycache__
       ├── models.py
       ├── __pycache__
       ├── tasks.py
       ├── templates
       │   └── thumbnailer
       │       └── home.html
       ├── tests.py
       ├── urls.py
       └── views.py
```
In our DOckerfile we'll need to specify the steps needed to build our image
```dockerfile
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
CMD celery worker -A image_parroter --loglevel=info
COPY . /code/
```

The next step is to set up out docker-compose file, in order to start our containers and adding them to the same network.
```bash
project
   ├── django-app
   ├── docker-compose.yml
```


To do that we'll add the lines below to our docker-compose.yml
```yml
version: '3'
services:
  db:
    image: postgres
  web:
    build: ./django-app
    command: python3 manage.py runserver 0.0.0.0:8000
    volumes:
      - ./django-app:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
```

To start the containers in detach mode run this command on the root dir of the proyect:
```bash
docker-compose up -d
```

Check if the container are runnint correctly with:
```bash
docker ps
```
> if you do not see the containers running or only one, the compose step was done wrong

The next step is to check if the django-server is running correctly in our container,
to do so simple navigate to http://localhost:8000, if you do not see your app running check the log of the container with the command:
```bash
docker exec logs -f <container_name>
```

If running correctly the next step is to start celery in our django contanier, to do that we'll need and interactive shell inside the container
```bash
docker exec -it <container_name> bash
```

Now inisde of the container run this command to start celery
```bash
celery worker -A image_parroter --loglevel=info
```

To set up our redis server in a digital-ocean dorplet, well need to connect to it via ssh with 
```bash
ssh <user>@<droplet_ip>
# eg
ssh root@127.0.0.1
```

Inside our droplet we'll need to set up redis, to do that we start by downloading it ans starting the service
```bash
apt update
apt install redis-server
```
We need one more step to setup the redis server, and that it's set the default ip  wich will bind to the redis instace
```bash
vim /etc/redis/redis.conf
```


In redis.conf we'll need to comment one line, wich by default it binds to local host, commenting this line we are making redis recive request from any client
```
# IF YOU ARE SURE YOU WANT YOUR INSTANCE TO LISTEN TO ALL THE INTERFACES
# JUST COMMENT THE FOLLOWING LINE.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# bind 127.0.0.1
```