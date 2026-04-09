# 1. Use Python as the base
FROM python:3.9-slim

# 2. Create a folder for the app
WORKDIR /app

# 3. Copy your app.py from GitHub into the container
COPY app.py .

# 4. Install Flask so the web server can run
RUN pip install flask

# 5. Tell the container to stay alive on port 8080
CMD ["python", "app.py"]
