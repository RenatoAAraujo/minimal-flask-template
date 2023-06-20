FROM python:3.10.3-alpine as base

COPY requirements.txt requirements-dev.txt /app/

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && apk add musl-dev gcc gzip\
    && pip3 install --upgrade pip

############# Debugger #############
FROM base as debug

RUN mkdir /.cache \
    && mkdir /.cache/pylint \
    && chmod 777 -R /.cache

RUN echo "Installing requirements-dev.txt" && pip install -r /app/requirements-dev.txt;

COPY . /app
WORKDIR /app

RUN chmod +x /app/app.py

ENTRYPOINT [ "python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "app.py" ]
# CMD python -m debugpy --listen 0.0.0.0:5678 app.py
############# Prod #############
FROM base as prod

RUN echo "Installing requirements.txt" && pip install -r /app/requirements.txt;

COPY . /app
WORKDIR /app

RUN chmod +x /app/app.py

ENTRYPOINT [ "python", "app.py" ]
