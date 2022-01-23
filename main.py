from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'wednesday'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'addams'
app.config['MYSQL_PASSWORD'] = 'family'
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