FROM python:3.8

RUN apt update && \
    apt install -y netcat-openbsd && \
    apt install -y gunicorn && \
    apt install -y uwsgi && \
    apt install -y uwsgi-plugin-python3

ENV INSTALL_PATH /api
RUN mkdir -p $INSTALL_PATH

ADD . $INSTALL_PATH
WORKDIR $INSTALL_PATH

RUN pip install -r $INSTALL_PATH/requirements.txt

RUN chmod +x docker_entrypoint.sh

CMD ["/bin/bash","docker_entrypoint.sh"]