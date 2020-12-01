import os
import bcrypt
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'database.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

@app.route("/Home")
def admin():
    username = request.cookies.get('username')
    usertype = "null"
    if 'usertype' in session:
        usertype = escape(session['usertype'])
    if usertype == "Admin":
        return render_template('home.html', msg = 'logged in as admin', username = username)
    else:
        return render_template('selectPDF.html', msg = 'no access', username = username)

app.secret_key = 'bqxe6dx12x7fxa9xd5xdcycxx04xdf4xb6chxca@;Pxdax02xcf' #using os.urandom(24)

@app.route("/Login", methods = ['GET','POST'])
def login():
    if request.method=='POST':
        uName = request.form.get('username', default="Error")
        pw = bcrypt.hashpw(request.form.get('password', default="Error").encode(),b'$2b$12$5nU0TVBvc2ZD2mLE6PztrO')
        # Hashes received password with the same salt as used for admin password
        # Tip: When hashing make sure to encode the string being passed to UTF-8
        if checkCredentials(uName, pw):
            print("checking login details")
            session['username'] = request.form['username']
            if (uName =="Admin"):
                session['usertype'] = 'Admin'
                resp = make_response(render_template('home.html', msg='hello '+uName, username = uName))
            else:
                session['usertype'] = 'Staff'
                resp = make_response(render_template('selectPDF.html', msg='hello '+uName, username = uName))
        else:
            resp = make_response(render_template('login.html', msg='Incorrect login'))
        return resp
    else:
        username = 'none'
        if 'username' in session:
            username = escape(session['username'])
        return render_template('Login.html', msg='', username = username)

def checkCredentials(uName, pw):
    return pw == b"$2b$12$5nU0TVBvc2ZD2mLE6PztrOcdB.SwZnfS5Ff7PK3rQYK.gjJtu967K"
    # Long string of characters is the hashed password for admin


@app.route("/Index")
def index():
    return render_template('index.html')

@app.route("/Users", methods=['GET'])
def users():
    if request.method == 'GET':
        username = request.cookies.get('username')
        usertype = "null"
        if 'usertype' in session:
            usertype = escape(session['usertype'])
        if usertype != "Admin":
            return render_template('selectPDF.html', msg = 'no access', username = username)
        db = sqlite3.connect("database.db")
        curs = db.cursor()
        curs.execute("SELECT username, role FROM Users")
        results = curs.fetchall()
        username_array = []
        role_array = []
        for idx, val in enumerate(results):
            username_array.append(results[idx][0])
            role_array.append(results[idx][1])
        print(username_array,role_array)
        curs.close()
        db.close()
        return render_template("users.html", usernames = username_array, roles = role_array)


@app.route("/FetchUser")
def fetchuserinfo():
    db = sqlite3.connect("database.db") # Opens the DB
    curs = db.cursor()
    curs.execute("SELECT username, role FROM Users") # Executes the SQL query
    results = curs.fetchall()
    # ^ Creates an array of tuples for the rows of the table with selected cols
    username_array = []
    role_array = []
    # Initializes 2 lists which will later be passed to users.html
    for idx, val in enumerate(results):
        username_array.append(results[idx][0])
        role_array.append(results[idx][1])
        # Appends the lists with the data required
    print(username_array,role_array)
    curs.close()
    db.close()
    # Closes the file to prevent memory leaks
    return render_template("users.html", username = username_array, role = role_array)
    # ^ Shows the user users.html with the required data

@app.route("/Customers")
def customer():
    if request.method == 'GET':
        username = request.cookies.get('username')
        usertype = "null"
        if 'usertype' in session:
            usertype = escape(session['usertype'])
        if usertype == "Admin":
            try:
                conn = sqlite3.connect(DATABASE)
                cur = conn.cursor()
                cur.execute("SELECT customerName, address, deliveryAddress FROM Customers") #check that this is secure as it doesn't use the "?"
                data = cur.fetchall()
                print(data)
            except:
                print('there was an error', data)
                conn.close()
            finally:
                conn.close()
                # return str(data)
                return render_template('customers.html', data = data)
        else:
            return render_template('selectPDF.html', msg = 'no access to customers page', username = username)

@app.route("/Customer/AddCustomer", methods = ['POST','GET'])
def add_customer():
    if request.method == 'POST':
        customerName = request.form.get('customerName', default="Error")
        address = request.form.get('address', default="Error")
        deliveryAddress = request.form.get('deliveryAddress', default="Error")
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO Customers ('customerName', 'address', 'deliveryAddress')\
            VALUES (?,?,?)",
            (customerName, address, deliveryAddress) )
            conn.commit()
            msg = "Record successfully added"
        except Exception as e:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return msg

if __name__ == "__main__":
	app.run(debug=True)
