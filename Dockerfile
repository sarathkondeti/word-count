# Build command: docker build -t simple-rest-api .
# Run command:   docker run -p 5000:5000 simple-rest-api



# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY app.py /app/
COPY requirements.txt /app/

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask to run on
EXPOSE 5000

# Define the command to run your Flask app
CMD ["python", "app.py"]
