# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/smileInflatables

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y netcat-openbsd

# copy project
COPY . .
RUN sed -i 's/\r$//g' /usr/src/smileInflatables/entrypoint.sh
RUN chmod +x /usr/src/smileInflatables/entrypoint.sh

ENTRYPOINT ["/usr/src/smileInflatables/entrypoint.sh"]
