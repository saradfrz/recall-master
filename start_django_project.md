# Create Folder structure

## Start the project

1. First, create a new Django project:
```bash
django-admin startproject myproject
```

2. Navigate into the project directory:
```bash
cd myproject
```

3. Create two Django apps within the project:
```bash
python manage.py startapp home
python manage.py startapp game01
```

4. Your folder structure will look like this:
```
myproject/
│
├── home/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── game01/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

5. In your `settings.py` file, add the two apps to the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
    ...
    'home',
    'game01',
    ...
]
```

## Create the templates folder


1. Create a `templates` folder at the root of your Django project:

```
myproject/
├── myproject/
├── home/
├── game01/
└── templates/
    ├── base.html
    ├── home/
    │   └── home.html
    └── game01/
        └── game01.html
```

2. In your Django settings (`settings.py`), you need to specify the location of the `templates` folder. Add the following line to your settings file:

```python
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Specify the location of the templates folder
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add this line
        ...
    },
]
```

With this configuration, Django will now also search for templates in the `templates` folder at the root of your project in addition to the app directories. You can place your HTML templates in this folder as needed.


In Django, you typically create a `static` folder at the root of your Django project to store static files such as CSS, JavaScript, images, etc. Here's how you can do it:

## Create the static folder

1. Create a `static` folder at the root of your Django project:

```
myproject/
├── myproject/
├── home/
├── game01/
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── scripts.js
│   └── images/
│       └── example.jpg
└── templates/
    ├── base.html
    ├── home/
    │   └── home.html
    └── game01/
        └── game01.html
```

2. Inside the `static` folder, you can create subfolders to organize your static files. For example:
   - `css`: Store CSS files.
   - `js`: Store JavaScript files.
   - `images`: Store image files.

3. Place your static files (e.g., CSS, JavaScript, images) inside their respective subfolders in the `static` folder.

4. Ensure that your static files are properly configured in your Django settings (`settings.py`). You'll need to specify the location of the `static` folder and configure Django to serve static files during development.

In your Django settings (`settings.py`), make sure you have the following configurations:

```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```