FROM python:3.10

WORKDIR /app

COPY ./app /app/app

RUN pip install fastapi uvicorn sqlalchemy

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
