FROM python:3.6

EXPOSE 5000
EXPOSE 3306
EXPOSE 80

WORKDIR /addamsapp

COPY ./app ./app
COPY ./Unit_test ./Unit_test
COPY ./docs ./docs
RUN pip3 install -r app/requirements.txt
#RUN apt-get update
#RUN apt-get install python3-sphinx -y
#RUN apt-get install apache2 -y
#RUN cd docs/ && make html && cd .. && cp -r docs/_build/html /var/www/ && 
#RUN /etc/init.d/apache2 start
#RUN /etc/init.d/apache2 restart
#CMD python3 app.py 
#RUN sleep 30
RUN chmod +x app/start.sh
CMD ./app/start.sh