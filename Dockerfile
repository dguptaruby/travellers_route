FROM python:3.8
RUN mkdir /travelling_salesman
WORKDIR /travelling_salesman
ADD . /travelling_salesman
RUN pip install -r requirement.txt
EXPOSE 8000
CMD python manage.py runserver 0:8000