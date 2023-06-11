FROM python:3.9-slim-buster
 
# Install wkhtmltopdf dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libxrender1 \
    libfontconfig1 \
    libx11-dev \
    libjpeg62-turbo-dev \
    libxtst6 \
    xz-utils \
    wkhtmltopdf \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
 
# Install Python packages
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy Python script
COPY app.py .
 
# Run Python script
CMD ["python", "app.py"]
