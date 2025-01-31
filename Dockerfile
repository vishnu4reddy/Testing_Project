# Use a base image with Python
FROM python:3.11-slim

# Set the working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    libglib2.0-0 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js and Playwright
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g playwright

# Install Poetry
RUN pip install poetry

# Install dependencies
COPY pyproject.toml /workspace/
RUN poetry install

# Copy the rest of the application
COPY . /workspace/

