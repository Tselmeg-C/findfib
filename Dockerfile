# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /home/tmp

# copy the dependencies file to the working directory
COPY . .

# install dependencies
RUN pip install -r requirements.txt
RUN pip install .

EXPOSE 5000

# command to run on container start
CMD [ "python", "./app.py" ]