FROM python:3.6.0-alpine

COPY . /code
RUN pip install -e /code
RUN python /code/manage.py collectstatic --clear --no-input
