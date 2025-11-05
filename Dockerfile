FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install OS packages
RUN apt update -y && apt install -y awscli

# Copy everything
COPY . .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .

# Expose port
EXPOSE 8080

# Run app
CMD ["python3", "app.py"]
