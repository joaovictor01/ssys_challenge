# ssys_challenge

### Dependencies

Istall the requirements

```
pip3 install -r requirements.txt
```

### How to use

Create an MySQL user ```root``` with password ```root```
Create an database with the name ```ssys_challenge```
```
mysql -uroot -p
create database ssys_challenge;
```
export the flask environment variables:
```
 export FLASK_APP=main.py
 export FLASK_ENV=development
```
Init the db and do the migrations
```
  flask db init
  flask db migrate
  flask db upgrade
```

then start the API:

```
  flask run
```
To use the api, import the ```ssys.postman_collection.json``` on Postman, then on Postman:
Register -> Login

Copy the token generated and use as Bearer token to make requests to the API




