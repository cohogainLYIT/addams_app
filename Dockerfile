FROM python:3.6

EXPOSE 5000
EXPOSE 3306
EXPOSE 80

WORKDIR /addamsapp

COPY ./app ./app
COPY ./Unit_test ./Unit_test
COPY ./docs ./docs

RUN pip3 install -r app/requirements.txt
RUN pip3 install -r Unit_test/requirements.txt

RUN pytest Unit_test/bench.py --benchmark-json output.json
RUN chmod +x app/start.sh
CMD ./app/start.sh