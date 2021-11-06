# Django

#. Create tables::
    psql -d code.djangoproject < tracdb/trac.sql

    ./manage.py migrate
    python3 manage.py migrate

#. Create a superuser::

   ./manage.py createsuperuser
   python3 manage.py createsuperuser

#. Populate the www and docs hostnames in the django.contrib.sites app::

    ./manage.py loaddata dev_sites

Commands-Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. Get version Django::
    django-admin --version
#. Create Project Django    
    django-admin startproject sena


Running Locally with Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Build the images::

    docker-compose build

2. Spin up the containers::

    docker-compose up

3. View the site at http://localhost:8000/

4. Run the tests::

    docker-compose exec web tox
    docker-compose exec web python manage.py test
