## IMAGE API with Django, DJANGO_REST_FRAMEWORK, Cloudinary and Tailwind CSS

technologies: <a href="https://docs.djangoproject.com/">django</a>, <a href="https://www.django-rest-framework.org/">django rest framework</a> , <a href="https://cloudinary.com">Cloudinary</a> and <a href="https://tailwindcss.com/">Tailwind</a>


## Project setup

- Create a virtual environment
```bash
python -m venv venv
```
- Activate the environment
    - windows
    ```bash
    .\venv\scripts\activate
    ```
    - MacOs or Linux
    ```bash
    source venv/bin/activate
    ```

- install the requirements
```bash
pip install -r requirements.txt
```

- set values in  <b>.env</b>
```python
DJANGO_DEBUG=True
DJANGO_SECRET_KEY="django-secret-key"
CLOUDINARY_API_KEY="api-key"
CLOUDINARY_NAME="cloudinary-name"
CLOUDINARY_SECRET_KEY="cloudinary-secret-key"
```

- working dir
```bash
cd src/
```
- Generate <i>DJANGO_SECRET_KEY</i>
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

- Migrate
```bash
python manage.py migrate
```

- Run the server
```bash
python manage.py runserver
```