from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import sys
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import mysql.connector
import requests

import os

os.environ.get('FLASK_ENV')

if os.environ.get('FLASK_ENV') == 'production':
    dbhost="db"
else:
    dbhost='db_dev'

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = dbhost
app.config['MYSQL_USER'] = 'addams'
app.config['MYSQL_PASSWORD'] = 'family'
app.config['MYSQL_DB'] = 'addams'
app.config['MYSQL_PORT'] = 3306

# Intialize MySQL
mysql = MySQL(app)

@app.route('/makeres2', methods=['POST'])
def makeres2():
    """
        **makeres2**

        :return dictFromServer


    """
    event_data = request.get_json()
    print(event_data, file=sys.stderr)
    response = requests.post('http://127.0.0.1:5000/getAccomodations', json=event_data)
    print(response.text, file=sys.stderr)
    dictFromServer = response.text
    return dictFromServer


@app.route('/getAccomodations', methods=['POST'])
def getaccomodations():
    """ 

        **getAccomodations**

        API call which triggers CreateBooking store procedure and matches available room
        to booking details provided.

        :return: html page informing you if your booking is successful or has failed

        - Example::

            name = Adam Addam
            date = 08/02/2022
            guests = 2
            property = Creepy Caravan
        
        - Expected Success Response:: 

            Renders book_success.html with booking details
            HTTP Status Code: 200
            "Booking Successful!"
        
        - Expected Fail Response::

            Renders book_fail.html
            HTTP Status Code: 200
            "Booking failed."

    """ 
    requestbody = request.get_json()
    print("Print This", file=sys.stderr)

    print(requestbody, file=sys.stderr)
    print(requestbody['nice_to_have'], file=sys.stderr)

    reservation_name = requestbody['reservation_name']
    reservation_date = requestbody['reservation_date']
    nice_to_have = requestbody['nice_to_have']
    guests = int(requestbody['guests'])

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("CALL CreateBooking('{0}', '{1}', {2}, '{3}')".format(reservation_name, reservation_date, guests, nice_to_have))

    bookingdetails = cursor.fetchone()
    print(bookingdetails, file=sys.stderr)

    print(bookingdetails['accomodation'], file=sys.stderr)
    accomodation = bookingdetails['accomodation']
    reservation_date = bookingdetails['reservation_date']
    booking_id = bookingdetails['booking_id']
    
    if bookingdetails != 'None':
        return render_template('book_success.html', name=reservation_name, num=guests, date=reservation_date, property=accomodation,nice_to_have=nice_to_have)
    else:
        return render_template('book_fail.html')


@app.route('/admin/', methods=['GET','POST'])
def index():
    """
    
    """
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
    """ 

        **Delete method**

        Deletes booking record from mysql bookings table.

        :param id_data: id of booking
        :type id_data: int


        - Example::

            id_data = 4
        
        - Expected Success Response:: 

            HTTP Status Code: 200
            Record Has Been Deleted Successfully

    """
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM bookings WHERE booking_id = %s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))

@app.route('/', methods=['GET', 'POST'])
def book():
    """ 



    """

    # Output message if something goes wrong...
    msg = ''
        # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'reservation_name' in request.form and 'reservation_date' in request.form and 'guests' in request.form :
        # Create variables for easy access
        reservation_name = request.form['reservation_name']
        reservation_date = request.form['reservation_date']
        guests = request.form['guests']
        nice_to_have = request.form['nice_to_have']


        event_data = { "reservation_name":reservation_name, "reservation_date":reservation_date, "guests":guests, "nice_to_have":nice_to_have}
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

# http://localhost:5000/pythonlogin/ - the following will be our login page, which will use both GET and POST requests
@app.route('/login/', methods=['GET', 'POST'])
def login():
    """ 
        **Login page**

        Checks login credentials against accounts mysql table and grants access if account and credentials exists.

        - Example::

            username = Adam_Addam
            password = Bo0!
        
        - If credentials exists:: 

            :return: home.html
        
        - If credentials do not exists:: 

            Incorrect username/password!
            :return: index.html

    """
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
        print(cursor, file=sys.stderr)

        # Fetch one record and return result
        account = cursor.fetchone()
        print(account, file=sys.stderr)

        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('home'))        
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)


# http://localhost:5000/python/logout - this will be the logout page
@app.route('/logout')
def logout():
    """
    
    """
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('login'))


# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
        **Registration page**

        Registers user credentials as account if provided credentials do not already exist and meet requirements.

         - If username already in accounts database:: 

            Account already exists!
        
        - If email not correct format::

            Invalid email address!

         - If username not correct format:: 

            Username must contain only characters and numbers!
        
        - If credentials meet requirements and not in database::

            You have successfully registered!

    """
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/home')
def home():
    """
        **Home page**

        Home page accessible only by users logged in.

         - If user is logged in:: 

            :return: home.html
        
        - If user not logged in::

            :return: login.html

    """
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


# http://localhost:5000/pythinlogin/profile - this will be the profile page, only accessible for loggedin users
@app.route('/profile')
def profile():
    """
        **Profile page**

        Profile page accessible only by users logged in.

         - If user is logged in:: 

            :return: profile.html
        
        - If user not logged in::

            :return: login.html

    """
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))
    