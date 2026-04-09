# Use a Python base image
FROM python:3.9-slim

# Set the location inside the container for your code
WORKDIR /app

# Copy your app.py from GitHub into the container
COPY . /app

# Install the web server library (Flask)
RUN pip install flask

# Tell the container to listen on port 8080
EXPOSE 8080

# The command to start the server and KEEP IT RUNNING
CMD ["python", "app.py"]
