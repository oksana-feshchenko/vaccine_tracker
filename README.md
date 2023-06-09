
## Django Vaccination Tracker
A web application for tracking the vaccination records of children.
Parents can register an account and add their children's vaccination
records to the system. They can view a history of all vaccinations 
for each child, as well as any complications that occurred as a result
of the vaccinations.


![img_2.png](img_2.png)!

## Check it out
Render: https://vaccination-tracker.onrender.com/
Repository:https://github.com/oksana-feshchenko/vaccine_tracker.git
![Demo](img_1.png)

## Getting started
To get started with the Django Vaccination Tracker, you can follow these steps:

Clone the repository:
``` shell
git clone https://github.com/oksana-feshchenko/vaccine_tracker.git
```
Navigate to the project directory:
``` shell
cd vaccination-tracker
```
Install the required packages:
``` shell
 pip install -r requirements.txt
 ```
Run migrations:
``` shell
python manage.py migrate
```
Create a superuser:
 -You can use following superuser (or create another one by yourself):

```shell
login:admin_user
password: qwerty
```

``` shell 
python manage.py createsuperuser
```
Start the development server:
``` shell
python manage.py runserver
```

## Features
Parents can create an account and add their children's vaccination records.
View a history of all vaccinations for each child.
View any complications that occurred as a result of the vaccinations.




