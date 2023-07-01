FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP=index.py
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "index:app"]
