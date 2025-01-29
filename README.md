<h1 align="center">Welcome on the readme Django Wagtail Tailwind blog 👋</h1>
<p align="center">
  <a href="https://twitter.com/LaurentJouron">
    <img alt="Twitter: LaurentJouron" 
      src="https://img.shields.io/twitter/follow/LaurentJouron.svg?style=social" target="_blank" />
  </a>
  <a href="https://github.com/LaurentJouron">
    <img alt="GitHub followers" 
      src="https://img.shields.io/github/followers/LaurentJouron?style=social" />
  </a>
</p>

___________

<h1 align="center">Getting the files</h1>

* Download zip file 
or
* git clone command (need git to be installed) and remove git folder afterwards
```
git clone https://github.com/LaurentJouron/Django_Wagtail_Tailwind_blog.git . && rm -rf .git
```

<h1 align="center">Setup</h1>

* Create Virtual Environment

```
mkdir .venv
```
```
pipenv install
```
```
pipenv shell
```

<h1 align="center">Build container project with Docker</h1>

```
docker compose up -d
```

<h1 align="center">Migrate to database</h1>

```
python manage.py migrate
```
```
python manage.py createsuperuser
```

<h1 align="center">Run frontend</h1>

```
cd frontend
```
* for watch
```
npm run tailwind-watch
```
* for minify build
```
npm run tailwind-build
```

<h1 align="center">Run application</h1>

```
python manage.py runserver
```

<h1 align="center">Generate Secret Key (! Important for deployment !)</h1>

```
python manage.py shell
```
```
from django.core.management.utils import get_random_secret_key
```
```
print(get_random_secret_key())
```
```
exit()
```
