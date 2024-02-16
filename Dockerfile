FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py
COPY movie_review_classifier.joblib movie_review_classifier.joblib

RUN pip install -r requirements.txt

EXPOSE  5000

CMD ["python", "app.py"]
