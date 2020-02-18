FROM python:3.8.0-alpine


RUN apk update && \
    apk add --no-cache --virtual build-deps \
    openssl-dev libffi-dev gcc python3-dev musl-dev \
    postgresql-dev netcat-openbsd




ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app


COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh


COPY . /usr/src/app