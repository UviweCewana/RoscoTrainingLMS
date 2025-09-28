FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn[standard] databases[postgresql] sqlalchemy psycopg2-binary
CMD ["uvicorn", "webhook_receiver:app", "--host", "0.0.0.0", "--port", "8000"]
