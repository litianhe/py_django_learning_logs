# 18.1.3 install venv:
`pip install virtualenv`

# 18.1.2 create venv:
`python -m venv django36`

# 18.1.4 activate venv:
`source django36/bin/activate`

# 18.1.5 install django
`pip install Django`

# 18.1.6 create learning_log project
`django-admin.py startproject learning_log .`

# 18.1.7 create db
`python manage.py migrate`

# 18.1.8 test run 
`python manage.py runserver`

# 18.2 create app
`source django36/bin/activate`

`python manage.py startapp learning_logs`

# 18.2.1 create model
more models refer to: https://docs.djangoproject.com/en/1.8/ref/models/fields/

# 18.2.2 activate models
1. modify settings.py
2. `python manage.py makemigrations learning_logs`
3. `python manage.py migrate`

note: update the managed data, should follow flow 1-2-3 above.

# 18.2.3 (1) create superuser "root"/P0!"
`python manage.py createsuperuser`

# 18.2.3 (2) register model to super user site by modify admin.py

# Milestone: success to access django web site from docker host network 192.168.6.x, not only on local network
             success to access http://192.168.6.x:8001 and http://192.168.6.x:8001/admin
1. modify settings.py , add ALLOWED_HOST
2. modify ~/.bashrc , add 2 lines below:
   `cd /django`
   `source django36/bin/activate`
   exit and re-enter container.
3. run `python manage.py runserver 0.0.0.0:8001`

# 18.2.7 Django shell
`python manage.py shell`

```
from learning_logs.models import Topic`

topics = Topic.objects.all()`

for t in topics:
  print(t.id, t)

## access 'entry' via foreinKey using <model>_set , each Entry is connected to one Topic.
t1 = topics[0]
t1.entry_set.all()
```
ctrl+D to exit shell on linux


# Django Reference
## Django API
https://docs.djangoproject.com/en/3.1/topics/db/queries/


## Django tutorial 
https://docs.djangoproject.com/en/3.0/intro/


## Django template
https://docs.djangoproject.com/en/3.0/ref/templates/

## Rebuild db in django shell
```
python manager.py flush
```

## bootstrap3 examples
http://getbootstrap.com/getting-started/#examples

