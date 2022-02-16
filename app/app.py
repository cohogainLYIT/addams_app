from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
#import re
import mysql.connector
#import json
import sys
#import logging
import requests
import os

os.environ.get('FLASK_ENV')

if os.environ.get('FLASK_ENV') == 'production':
    dbhost="db"
else:
    dbhost='db_dev'

mydb = mysql.connector.connect(
  #host="127.0.0.1",
  host=dbhost,
  user="addams",
  password="family",
  database="addams",
  port = 3306
)

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
# app.secret_key = 'wednesday'

# Enter your database connection details below
#app.config['MYSQL_HOST'] = 'db'
#app.config['MYSQL_USER'] = 'addams'
#app.config['MYSQL_PASSWORD'] = 'family'
#app.config['MYSQL_DB'] = 'addams'

# Intialize MySQL
#mysql = MySQL(app)


@app.route('/makeres2', methods=['POST'])
def makeres2():
    # event_data = { "reservation_name":"KK", "reservation_date":"2022-02-22", "guests":7}
    event_data = request.get_json()
    print(event_data, file=sys.stderr)
    response = requests.post('http://127.0.0.1:5000/getAccomodations', json=event_data)
    print(response.text, file=sys.stderr)
    dictFromServer = response.text
    return dictFromServer

@app.route('/getAccomodations', methods=['POST'])
def getaccomodations():
    # Output message if something goes wrong...
    msg = ''
        # Check if "username" and "password" POST requests exist (user submitted form)
    requestbody = request.get_json()
    print("Print This", file=sys.stderr)

    print(requestbody, file=sys.stderr)

    reservation_name = requestbody['reservation_name']
    reservation_date = requestbody['reservation_date']
    guests = int(requestbody['guests'])

    mycursor = mydb.cursor()

    command = "CALL CreateBooking('{0}', '{1}', {2})".format(reservation_name, reservation_date, guests)
    results = mycursor.execute(command, multi=True)

    try:
        for result in results:
            if result.with_rows:
                bookingdetails = result.fetchall()
    except Exception as e:
        pass
    print(bookingdetails, file=sys.stderr)
    if bookingdetails:
        return "You have been booked into {0} on {1}. Booking Reference: {2}".format(str(bookingdetails[0][0]),str(bookingdetails[0][1]),str(bookingdetails[0][2]))
    else:
        return "No Available Rooms for your number of guests"


@app.route('/', methods=['GET', 'POST'])
def book():
    # Output message if something goes wrong...
    msg = ''
        # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'reservation_name' in request.form and 'reservation_date' in request.form and 'guests' in request.form :
        # Create variables for easy access
        reservation_name = request.form['reservation_name']
        reservation_date = request.form['reservation_date']
        guests = request.form['guests']

        event_data = { "reservation_name":reservation_name, "reservation_date":reservation_date, "guests":guests}
        response = requests.post('http://127.0.0.1:5000/getAccomodations', json=event_data)
        print(response.text, file=sys.stderr)
        dictFromServer = response.text
        return dictFromServer
        # Check if account exists using MySQL
        #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #cursor.execute('insert into bookings values(%s, %s, %s)', (reservation_name, reservation_date, guests,))
        #mysql.connection.commit();
        #cursor.execute('SELECT * FROM bookings WHERE reservation_name = %s AND reservation_date = %s AND guests = %s', (reservation_name, reservation_date, guests,))
        # If account exists in accounts table in out database
        #booking = cursor.fetchone()
        #if booking:
        #    return 'Thank you for your booking!'
        #else:
        #    msg = 'Apologies but your booking failed'
    return render_template('booking.html', msg='')

@app.route('/login/', methods=['GET','POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
        # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('index'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'

    return render_template('login.html', msg='')

@app.route('/admin/', methods=['GET','POST'])
def index():
    if not session.get("loggedin") is None:
        if session['loggedin'] == True:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM bookings')
            reservation_data = cursor.fetchall()
            cursor.close()
            for reservation in reservation_data:
                print(reservation)
            return render_template('admin.html', reservation_data=reservation_data )
    else:
        return redirect(url_for('login'))


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM bookings WHERE reservation_date = %s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))

#if __name__ == '__main__':
#    app.run(debug=True)