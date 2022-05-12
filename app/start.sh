#!/bin/bash
if [ "$FLASK_ENV" == "development" ]
then
    apt-get update
    apt-get install python3-sphinx -y
    apt-get install apache2 -y
    pip3 install sphinx_rtd_theme
    cd docs/
    sphinx-apidoc -o . ..
    make clean
    make html
    cd .. 
    cp -r docs/_build/html /var/www/
    /etc/init.d/apache2 start
    cd Unit_test
    pip install -r requirements.txt
    pytest bench.py --benchmark-json output.json
else
echo "Sleeping 15 seconds for mysql DB to come online"
sleep 15
fi
cd app
python3 -m flask run --host=0.0.0.0