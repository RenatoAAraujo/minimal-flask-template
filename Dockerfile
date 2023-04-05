FROM python:3.10.3-alpine

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && apk add musl-dev gcc tzdata gzip\
    && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
    && echo "America/Sao_Paulo" >  /etc/timezone \
    && apk del tzdata \
    && pip3 install --upgrade pip

WORKDIR /app
COPY requirements.txt .
COPY requirements-dev.txt .

RUN mkdir /.cache \
    && mkdir /.cache/pylint \
    && chmod 777 -R /.cache

ARG APP_ENV
RUN if [ "APP_ENV" == "production" ] ; then \
      echo "Installing requirements.txt" && pip install -r requirements.txt; \
    else \
      echo "Installing requirements-dev.txt" && pip install -r requirements-dev.txt; \
    fi

COPY docker_entrypoint.py /docker_entrypoint.py
RUN chmod +x /docker_entrypoint.py
COPY . .

CMD ["python", "/docker_entrypoint.py" ]
