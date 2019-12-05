# pull official base image
FROM python:3.8.0-alpine

#Add User
RUN adduser -D airappv1

# set work directory
WORKDIR /airappv1

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /airapp/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /airappv1

RUN chown -R airappv1:airappv1 /airappv1

USER airappv1

#Port
EXPOSE 5002

#command
CMD ["gunicorn", "-b", "0.0.0.0:5002", "wsgi:app"]
#CMD ["python", "app.py"]