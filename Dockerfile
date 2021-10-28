# Python version
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN apt-get update && apt-get install python3-psycopg2 gdal-bin binutils libproj-dev libgdal-dev postgresql-client -y
RUN pip install psycopg2
RUN pip install -r requirements.txt
ENV GDAL_LIBRARY_PATH /usr/bin
# Copy project
COPY . /code/
# RUN python manage.py collectstatic --noinput