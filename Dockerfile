FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libpq-dev \
    python3-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=movie_project.settings

# Create static folder & collect static
RUN mkdir -p /app/static
RUN python manage.py collectstatic --noinput

# Start the app
CMD ["gunicorn", "movie_project.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "600"]
