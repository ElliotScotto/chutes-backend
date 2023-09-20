# Use the official Python image from the DockerHub
FROM python:3.11.5

# Set the environment variable to ensure output is sent directly to terminal without buffering 
ENV PYTHONUNBUFFERED 1

# Create and set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Note: You don't need to create the /app directory manually since the WORKDIR instruction creates it for you.
# Therefore, I've removed the "RUN mkdir /app" command.

# Copy the rest of the application code to the working directory
COPY . /app/

# Default command to run the application using Gunicorn
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]