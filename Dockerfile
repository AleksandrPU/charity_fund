FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -U pip --no-cache-dir && pip install -r requirements.txt --no-cache-dir

#COPY . .
ADD app app
ADD alembic alembic
COPY alembic.ini .

#COPY entrypoint.sh .
#RUN chmod +x entrypoint.sh

#ENTRYPOINT ["entrypoint.sh"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]
