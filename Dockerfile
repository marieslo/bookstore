FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies (including build tools for psycopg2)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY . /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 8000

# Set the default environment for Django settings
ENV DJANGO_SETTINGS_MODULE=bookstore.settings

# Run the application when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
