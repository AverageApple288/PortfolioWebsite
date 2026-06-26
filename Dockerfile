# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the Flask port
EXPOSE 5000

# Command to run the application (using Gunicorn for production)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]