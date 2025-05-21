# Use official Python image
FROM python:3.10-slim

# Set work directory inside container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port Flask will run on
EXPOSE 5001

# Run the app
CMD ["python", "run.py"]
