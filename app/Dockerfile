FROM python:3.6

EXPOSE 5000
EXPOSE 3306

WORKDIR /addamsapp

COPY ./ ./
RUN pip3 install -r requirements.txt
#CMD python3 app.py 
CMD sleep 30 && python3 -m flask run --host=0.0.0.0