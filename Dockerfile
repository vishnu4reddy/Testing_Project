# Use a base image with Python 3.11
FROM python:3.11-slim

# Set the working directory
WORKDIR /workspace

# Install system dependencies required for Playwright and other libraries
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

# Install Node.js (required by Playwright)
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

# Install Playwright (and all its dependencies)
RUN npm install -g playwright

# Install Poetry (for Python dependency management)
RUN pip install poetry

# Copy the pyproject.toml to the container and install dependencies
COPY pyproject.toml /workspace/
RUN poetry install

# Copy the rest of the application files into the container
COPY . /workspace/

# Expose the port for the application (optional, depends on the app)
EXPOSE 8080

# Set the default command (can be adjusted depending on your needs)
CMD ["pytest"]
