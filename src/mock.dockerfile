# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /temp_ms

# Copy the application code into the container from the local "backend" directory
COPY ./backend /temp_ms

# Install FastAPI and Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn

# Install Boto3 for S3
RUN pip install boto3

# Install libraries
RUN pip install -r requirements.txt

# Install AWS Config
# RUN apt-get install awscli

# RUN aws configure set aws_access_key_id AKIAX7PBSZEHX75OIE7N
# RUN aws configure set aws_secret_access_key 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
# RUN aws configure set region use-east-2

# Expose the port that FastAPI will run on
EXPOSE 8000

# Start the FastAPI application using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]





