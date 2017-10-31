# how to
## env setup
```shell
$sudo apt-get install python #install python
$sudo apt-get install curl
$curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
$python get-pip.py
$pip install virtualenv virtualenvwrapper

#/usr/bin/virtualenvwrapper.sh
$source /usr/bin/virtualenvwrapper.sh

$mkvirtualenv django
$pip install django
$pip install djangorestframework

$python manage.py runserver
```

## update models
```shell
python manage.py makemigrations ${app_name}
python manage.py sqlmigrate ${app_name} ${migration_number}
python manage.py migrate
```
