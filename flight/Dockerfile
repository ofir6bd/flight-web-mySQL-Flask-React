# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY flight/requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY flight .

EXPOSE 5000

# Set the command to run the Flask app
CMD [ "python", "routes.py" ]