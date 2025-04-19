# Use an official Python image as a base
FROM python:3.10.12

# Set the working directory
WORKDIR /api

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define the default command to run the app
CMD ["python", "app.py"]
