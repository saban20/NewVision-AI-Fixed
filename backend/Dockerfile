FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file first for better caching
COPY requirements-compatible.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements-compatible.txt

# Copy the rest of the application
COPY . .

# Generate model files at build time
RUN python generate_models_compatible.py

# Expose the port the app runs on
EXPOSE 5000

# Use gunicorn as the production server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "4", "app:app"]

# Development-only command (overridden by docker-compose)
# CMD ["python", "app.py"]

# Health check endpoint
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:5000/api/health || exit 1