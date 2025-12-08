# Use official Python image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc libpq-dev build-essential \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    poppler-utils \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g terser \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK packages (stopwords, wordnet, punkt, pros_cons)
RUN python -m nltk.downloader stopwords wordnet punkt pros_cons

# Copy Django project code
COPY . .

# Run uglification script
RUN chmod +x scripts/uglify-minify.sh && ./scripts/uglify-minify.sh

# Expose port (default for Railway)
EXPOSE 8000

# Run migrations and start server
CMD ["sh", "-c", "python manage.py migrate && gunicorn basicsite.wsgi:application --bind 0.0.0.0:8000"]
