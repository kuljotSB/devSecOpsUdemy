# use an official python runtime as a parent image
FROM winamd64/python:3

#set the working directory in the container
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . .

WORKDIR /app/src


# install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=webApp

# Run app.py when the container launches
CMD ["flask", "--app", "webApp", "run", "--host=0.0.0.0"]
