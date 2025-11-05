FROM python:3.12-slim-bookworm

# env
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# System packages
RUN apt-get update -y && apt-get install -y awscli && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy only dependency files first
COPY requirements.txt setup.py README.md /app/

# Install python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY src /app/src
COPY app.py /app/

# Install local package
RUN pip install .

# Expose port
EXPOSE 8080

# Start app
CMD ["python3", "app.py"]
