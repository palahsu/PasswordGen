
# 1. Use lightweight Python base image
FROM python:3.12-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency file
COPY Requirments.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r Requirments.txt

# 5. Copy application source code
COPY app.py .
COPY password_generator.py .

# 6. Expose Flask application port
EXPOSE 5000

# 7. Start Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

