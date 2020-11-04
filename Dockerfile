FROM python:3.8

EXPOSE 5000

WORKDIR /challenge

# Install any needed packages specified in requirements.txt
COPY requirements.txt /challenge
RUN pip install -r requirements.txt

COPY . /challenge

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

CMD flask run