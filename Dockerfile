# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

# Model to use, find the list at https://gpt4all.io/ (or https://gpt4all.io/models/models.json)
ENV MODEL=ggml-gpt4all-j-v1.3-groovy.bin

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True


# Working folder
ENV APP_HOME /app
WORKDIR $APP_HOME

# Download model
RUN mkdir models
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install wget
RUN wget -q https://gpt4all.io/models/$MODEL -O ./models/$MODEL

# Install production dependencies.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy code to the container image.
COPY . ./

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app