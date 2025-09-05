# use an official python 3.10 image as a parent image
FROM python:3.10-slim-buster

# set the working directory in the container
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

# install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# make port 5000 available to the world outside this container
EXPOSE 5000

# command to run the application
CMD ["python3", "app.py"]