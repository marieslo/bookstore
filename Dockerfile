FROM python:3.9-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app


RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*


COPY . /app/


RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8000


ENV DJANGO_SETTINGS_MODULE=bookstore.settings


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
