from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'wednesday'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'change_this_before_testing'
app.config['MYSQL_PASSWORD'] = 'change_this_before_testing'
app.config['MYSQL_DB'] = 'addams'

# Intialize MySQL
mysql = MySQL(app)

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
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('insert into bookings values(%s, %s, %s)', (reservation_name, reservation_date, guests,))
        mysql.connection.commit();
        cursor.execute('SELECT * FROM bookings WHERE reservation_name = %s AND reservation_date = %s AND guests = %s', (reservation_name, reservation_date, guests,))
        # If account exists in accounts table in out database
        booking = cursor.fetchone()
        if booking:
            return 'Thank you for your booking!'
        else:
            msg = 'Apologies but your booking failed'
    return render_template('booking.html', msg='')

