# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /temp_ms

# Copy the application code into the container (assuming it's in the ./src/backend directory)
COPY ./src/backend /temp_ms

# Install FastAPI and Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn

# Expose the port that FastAPI will run on
EXPOSE 8000

# Start the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
