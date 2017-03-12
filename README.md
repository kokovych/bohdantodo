## bohdantodo
This is my first django-project. I create this for learning in Django, Python etc.
This is lists of tasks. I realized registration with django allauth. Also in third part app I used crispy_forms.

For running this project I recommend you to use virtualenv.
In your directory create virtualenv. In linux it  looks like:

```
~ $ virtualenv your_env_name
```

than

```
~ $ source your_env_name/bin/activate
```

I used be default sqlite3 db. You can change it to your database in settings.py


```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
Also I used gmail account for confirmation registration in settings.py write your own login and password and change settings in
your account. Of course, if you want to use confirmation.

Don't forget to make
```
pip install requirements.txt
```
for instalation into virtualenv all required python modules.

Get start this project:

```
~ $ python manage.py runserver
```
Example of this project in web [here](https://bohdantodo.herokuapp.com/)
