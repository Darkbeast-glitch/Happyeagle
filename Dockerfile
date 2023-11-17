# syntax=docker/dockerfile:1



ARG PYTHON_VERSION=3.11.6
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1


ENV PYTHONUNBUFFERED=1



RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

# into this layer.
RUN python -m pip install -r requirements.txt

# Switch to the non-privileged user to run the application.

# Copy the source code into the container.
COPY . /app/

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.

CMD ["python","manage.py", "runserver"]
