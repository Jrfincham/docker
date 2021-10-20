# # set base image (host OS)
# FROM python:3.8
# # set the working directory in the container
# WORKDIR /code
# COPY . .
# RUN pip install flask

# # Update system
# RUN ["apt-get", "update"]
# RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
#   && tar xzvf docker-17.04.0-ce.tgz \
#   && mv docker/docker /usr/local/bin \
#   && rm -r docker docker-17.04.0-ce.tgz
# # Install nano
# RUN ["apt-get", "install", "-y", "nano"]
# # Install Dockerfile
# RUN ["apt-get", "install", "-y", "docker.io"]
# # command to run on container start
# CMD [ "python", "./app.py" ]

FROM python:3.8

WORKDIR /root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .