# Backend Odontia
This project was build with Django, Django-RestFramework

### Installation 
- This project requires NodeJS with NPM and python.
- This project works with Django, Django Rest Framework

**2. Run backend development server**
- Install all required dependencies for the project:
~~~
pip install -r requirements.txt
~~~
- Make migrations:
~~~
python manage.py makemigrations --settings=Backend.settings.dev
python manage.py migrate --settings=Backend.settings.dev --run-syncdb
~~~
- Create superuser:
~~~
python manage.py createsuperuser --settings=Backend.settings.dev
~~~
- Start backend development server.
~~~
python manage.py runserver --settings=Backend.settings.dev
~~~
- The backend project must be running in http://127.0.0.1:8000/
