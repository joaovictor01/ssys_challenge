# ssys_challenge

### Dependencies

Istall the requirements

```
pip3 install -r requirements.txt
```

### How to use

Run the docker with the following command on the first time:

```
 docker-compose build
```
and then:


```
 docker-compose up
```

To use the api, import the ```ssys.postman_collection.json``` on Postman, then on Postman:
First register then login,
after sending the login request on postman, a token will be returned. 

Copy the returned token and use as authorization method on the other requests as Bearer token.




