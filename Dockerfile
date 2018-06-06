FROM python:2.7.15

# create the log directory
RUN mkdir -p /var/log/applications/invoizpaid

# Creating base "src" directory where the source repo will reside in our container.
# Code is copied from the host machine to this "src" folder in the container as a last step.
RUN mkdir /src
WORKDIR /src
COPY . /src

RUN apt-get update
RUN apt-get install python-pip -y
RUN pip install django==1.11
RUN pip install jenkinsapi

# Expose web service and nodejs debug port
EXPOSE  8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
