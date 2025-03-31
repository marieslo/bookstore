FROM python:3.9-slim

# Ensure Python doesn't write bytecode and output isn't buffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install dependencies (gcc, libpq-dev, postgresql-client for Postgres)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY . /app/

# Upgrade pip and install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Render uses for dynamic port binding
EXPOSE $PORT

# Set the Django settings module environment variable to 'app.settings'
ENV DJANGO_SETTINGS_MODULE=app.settings

# Use Gunicorn to serve the app, binding to the dynamic port
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT app.wsgi:application"]