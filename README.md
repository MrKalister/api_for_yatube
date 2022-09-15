# API for social network Yatube
### Description:
Thanks to this project, your services have the ability to exchange data with yatube
***
### Technologies:
* Python 3.9.10
* Django 2.2.16
* Djangorestframework 3.12.4
* Pytest-pythonpath 0.7.3
* Djangorestframework-simplejwt 4.7.2
* Pillow 8.3.1
* PyJWT 2.1.0
* Requests 2.26.0
***
### Installation and launch:
1. Сlone the [repository](https://github.com/MrKalister/api_final_yatube.git)
```
git clone https://github.com/MrKalister/api_final_yatube.git
``` 
or use SSH-key:
```
git clone git@github.com:MrKalister/yatube_final.git
```
2. Install and activate the virtual environment
```
python -m venv venv
```
```
source venv/Scripts/activate
``` 
3. Install dependencies from the file requirements.txt
```
pip install -r requirements.txt
``` 
4. Make migrate:
```
python3 manage.py migrate
```
5. Start project in dev-mode:
```
python manage.py runserver
```
***
## Examples requests
Get a list of all publications:
```
http://127.0.0.1:8000/api/v1/posts/
```
***
## More information:
[Documentation](http://127.0.0.1:8000/redoc/)
***
## Author
Novikov Maxim
