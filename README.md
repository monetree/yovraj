## project setup

1. create virtualenv `virtualenv -p python3 env`
2. activate `source bin/activate`
3. install packages `pip install -r requirements.txt`

## Steps to run the application

1. python manage.py migrate
2. python manage.py runserver

## Api end points

1. http://127.0.0.1:8000/users/
2. http://127.0.0.1:8000/customers/

Note: You should have `mysql` installed in local with below setup

        """

            'NAME': 'soubhagya',
            'USER': 'root',
            'PASSWORD': 'Thinkonce',

        """
