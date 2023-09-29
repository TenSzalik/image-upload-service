# Image upload API

API that allows users to upload images in JPG and PNG formats and create thumbnails from them based on the user's tier. Details [here](/backend/docs/task_requirements.md).

*The project was made according to the requirements specified during HexOcean recruitment.*

## How to run

Navigate to the `/backend` directory:

- run `docker compose up --build`.

In the .env file there are hardcoded environment variables to get the project up and running quickly. You ~~can~~ should change them as you like.

## Endpoints

There are six endpoints under the host [0.0.0.0:8000](0.0.0.0:8000).

### Token

Authentication is handled by JWT. If you want to use another endpoint, you need to get the token first and then send it in the header.

You can pass the superuser created during docker container initialization as data:

- username: Hexocean2023
    
- password: hexfoobarbaz2023

**POST** `/api/token/`

**POST** `/api/token/refresh/`

#### example

```bash
curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' --data '{"username": "Hexocean2023","password": "hexfoobarbaz2023"}' http://127.0.0.1:8000/api/token/
```

```json
{"refresh": <refresh_token>,"access": <access_token>}
```

### Upload

POST endpoints allow you to upload images and return thumbnails. Thumbnails are determined by the user's level - [details](/backend/docs/task_requirements.md). The GET endpoint will return the user's path to all their images.

**GET** `/api/upload/`

**POST** `/api/upload/`

#### example (as enterprise tier)

```bash
curl -X POST -F image=@<image.jpg> -H "Authorization: Bearer <token>" 127.0.0.1:8000/api/upload/
```

```json
{"id":1,"image_original":"http://127.0.0.1:8000/images/ab480677-2b60-455a-a16f-c81d4348b8f2-original.jpeg","image_small":"http://127.0.0.1:8000/images/ab480677-2b60-455a-a16f-c81d4348b8f2-200.jpeg","image_medium":"http://127.0.0.1:8000/images/ab480677-2b60-455a-a16f-c81d4348b8f2-400.jpeg","image_custom":null}
```

### Expiration

Here you can create expiration links from 300 to 30_000 seconds. For the POST endpoint, pass the name of the created image, and you will GET the expiration link. The get endpoint is responsible for displaying the image.

**POST** `/api/expiration/`

**GET** `/api/expiration/`

#### example

```bash
curl -X POST -H "Authorization: Bearer <token>" -F available_to=300 -F image="<img_name.jpg>" 0.0.0.0:8000/api/expiration/
```

```bash
"0.0.0.0:8000/api/expiration/e758125d-2210-47bf-a935-be8f7dcc4b73"
```

### Other

You can also use Swagger:

- `/api/schema/swagger/`

Redoc:

- `/api/schema/redoc/`

Django admin (here users can be created):

- `/admin/`

Or regular Django REST browsable API:

- `/`

## Testing

- `docker exec -it <container_name> pytest`

## Other commands for developing

- `docker exec -it <container_name> pylint --load-plugin
s pylint_django --django-settings-module=hexocean.settings --recursive=y expiri
ng_url/ multimedia/ user_profile/ hexocean/ conftest.py`

- `docker exec -it <container_name> black .`
