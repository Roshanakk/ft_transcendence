# FT_TRANSCENDENCE

ft_transcendence is a full-stack web application developed as part of the curriculum at 42. It showcases advanced web development skills by combining a wide range of technologies to deliver a polished and feature-rich application.

<br>

# Table of Contents

1. [Features](#Features)
2. [Run the project](#Run-the-project)
3. [Technologies used](#Technologies-used)
4. [Fourth Example](#fourth-examplehttpwwwfourthexamplecom)

<br>

## Features


- **Secure Player Authentication:** Token-based login using JWT and optional Two-Factor Authentication (2FA) for enhanced security.
- **Remote players :** players can connect on different devices and play the same Pong game.
- **Direct Matchmaking System:** Quickly find opponents for a game with an efficient matchmaking algorithm.
- **Customizable Player Profiles:** Personalize profiles with avatars
- **Personal Game Dashboards and Statistics:** Access detailed statistics and game history through user-specific dashboards.
- **Multiple Game Modes:** Play 1v1 matches or participate in exciting tournaments.
- **Live chat :** send private messages to your friends and send them invitation links to tournaments

<br>

## Technologies used

### Front-End:

- Javascript: for dynamic and responsive content.

### Back-End:

- Django: For robust and scalable server-side development.
- JWT: For authentication and session management.

### Database:

- PostgreSQL: For reliable and efficient data storage.

### Deployment:

- Docker: For containerization and multi-service orchestration.
- Nginx: For reverse proxy and serving static assets.

<br>

## Run the project

<br>

**1. Clone the repository.**  

*not gonna tell you how :D*

<br>

**2. Create the `.env` file.** 

`.env` file should be created in the root directory of this repository.

```bash
# = = = = = = =
# PYTHON:
# = = = = = = =
PYTHONUNBUFFERED=1 # Prevents Python from writing pyc files to disc (equivalent to python -B option)
PYTHONDONTWRITEBYTECODE=1 # Prevents Python from buffering stdout and stderr (equivalent to python -u option)

# = = = = = = =
# DJANGO:
# = = = = = = =
DEBUG=True
SECRET_KEY='some_secret_words'
ALLOWED_HOSTS=*
DJANGO_SUPERUSER_EMAIL=admin@gmail.com
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=qetwry135246

# sosial accounts settings for django-allauth
GOOGLE_CLIENT_ID='see-the-NOTE-below'
GOOGLE_SECRET='see-the-NOTE-below'

42_CLIENT_ID='see-the-NOTE-below'
42_SECRET='see-the-NOTE-below'

# = = = = = = =
# POSTGRES:
# = = = = = = =
# for PostgreSQL as well as Django in separate docker containers:
DATABASE_URL=postgres://postgres:postgres@db:5432/postgres

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres

```

<br>


- `make up` command will build the images, create the containers and run the project.
- `make re` command will remove the containers, volumes, rebuild the images and run the project.


