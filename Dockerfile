FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -U pip --no-cache-dir && pip install -r requirements.txt --no-cache-dir

ADD app app
ADD alembic alembic
COPY alembic.ini .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
