FROM python:3.7-alpine

RUN pip install flask

COPY ./src /app

ENV FLASK_APP=/app/app.py

CMD ["flask", "run", "--host=0.0.0.0"]
