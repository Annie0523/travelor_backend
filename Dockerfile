# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn

# Set environment variables
ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8402"
ENV FLASK_ENV=production

# Make port 8402 available to the world outside this container
EXPOSE 8402

# Run gunicorn server
CMD ["gunicorn", "main:app"]
