FROM python:3.10.2-slim

WORKDIR /app

ARG APP_DATA_FOLDER

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN dvc remote add -d myremote gdrive://$APP_DATA_FOLDER -f
RUN dvc remote modify myremote gdrive_use_service_account true
RUN dvc remote modify myremote gdrive_acknowledge_abuse true
RUN dvc push

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]