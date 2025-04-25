# Use a slim Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Playwright system dependencies
RUN apt-get update && apt-get install -y wget gnupg
RUN apt-get install -y fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libcups2 libdbus-1-3 libgdk-pixbuf2.0-0 libnspr4 libnss3 libx11-xcb1 xdg-utils

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Playwright browsers
RUN playwright install

# Download SpaCy English model
RUN python -m spacy download en_core_web_sm

# Copy application code
COPY . .

# Expose API port
EXPOSE 8000

# Default command: just run uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
