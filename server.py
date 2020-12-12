import os
import bcrypt
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3
import pdfkit

DATABASE = 'database.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
path_wkhtmltopdf = r'wkhtmltox/bin/wkhtmltopdf.exe'
CONFIG = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

app = Flask(__name__)

def checkAdmin():
    usertype = "null"
    if "usertype" in session:
        usertype = escape(session['usertype'])
    return usertype == "Admin"

@app.route("/Home")
def admin():
    username = request.cookies.get('username')
    if checkAdmin():
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
        # Tip: When hashing make sure to encode the string being passed to UTF-8 (.encode() by default is UTF-8)
        print(checkCredentials(uName, pw))
        if checkCredentials(uName, pw):
            print("checking login details")
            session['username'] = request.form['username']
        #new login method using databse
            try:
                conn = sqlite3.connect(DATABASE)
                cur = conn.cursor()
                cur.execute("SELECT * FROM Users WHERE username=?;", [uName])
                data = cur.fetchall()
                for idx, val in enumerate(data):
                    db_role = data[idx][6] #fetches role from database
            except:
                print('there was an error')
                conn.close()
            finally:
                conn.close()
            if db_role == "Admin": #checks that matching role from username is admin
                session['usertype'] = 'Admin'
                resp = make_response(render_template('home.html', msg='hello '+uName, username = uName))
            else:
                session['usertype'] = 'Staff'
                resp = make_response(render_template('selectPDF.html', msg='hello '+uName, username = uName))

            #previous method kept in for now but commented out
            # if (uName =="Admin"):
            #     session['usertype'] = 'Admin'
            #     resp = make_response(render_template('home.html', msg='hello '+uName, username = uName))
            # else:
            #     session['usertype'] = 'Staff'
            #     resp = make_response(render_template('selectPDF.html', msg='hello '+uName, username = uName))
        else:
            resp = make_response(render_template('login.html', msg='Incorrect login'))
        return resp
    else:
        session['usertype'] = None
        session['username'] = None
        rendered = render_template('Login.html', msg='')
        return rendered


def checkCredentials(uName, pw):
    #new login method using databse
    db_pass = None #avoids error if user has incorrect details
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Users WHERE username=?;", [uName])
        data = cur.fetchall()
        for idx, val in enumerate(data):
            db_pass = data[idx][5] #fetches password from database
    except:
        print('there was an error')
        conn.close()
    finally:
        conn.close()
    return str(pw) == db_pass #compares database password with inputed password. Only compares hashed values

    #previous method kept in for now but commented out
    #return pw == b"$2b$12$5nU0TVBvc2ZD2mLE6PztrOcdB.SwZnfS5Ff7PK3rQYK.gjJtu967K"
    # Long string of characters is the hashed password for admin




@app.route("/Index")
def index():
    return render_template('index.html')

@app.route("/Users", methods=['GET'])
def users():
    if request.method == 'GET':
        if session['usertype'] == None:
            return render_template('login.html', msg='Log in to use site')
        else:
            username = request.cookies.get('username')
            if not checkAdmin():
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

@app.route("/SelectPDF")
def selectpdfpage():
    if session['usertype'] == None:
        return render_template('login.html', msg='Login to use site')
    else:
        db = sqlite3.connect("database.db") # Opens the DB
        curs = db.cursor()
        curs.execute("SELECT pdfName FROM Orders") # Executes the SQL query
        pdfNames = curs.fetchall()
        # Initializes pdfNames list which will be passed onto selectPDF.html
        print(pdfNames)
        curs.close()
        db.close()
        # Closes the file to prevent memory leaks
        return render_template("selectPDF.html", pdfNames = pdfNames)

@app.route("/EditorPDF", methods = ['POST','GET'] )
def editorPDF():
    if request.method == 'GET':
        if session['usertype'] == None:
            return render_template('login.html', msg='Log in to use site')
        if checkAdmin():
            db = sqlite3.connect("database.db")
            prodcurs = db.cursor()
            prodcurs.execute("SELECT productName FROM items")
            Products  = prodcurs.fetchall()
            prodcurs.close()
            custcurs = db.cursor()
            custcurs.execute("SELECT customerName FROM Customers")
            Customers  = custcurs.fetchall()
            custcurs.close()
            db.close()
            print(Customers)
            return render_template("editorPDF.html", productName = Products , customerName = Customers)
    if request.method == 'POST':
        return render_template("HtmlToPdf.html") #Temporary Location

@app.route("/PDF")
def HtmlToPdf():
    rendered = render_template("HtmlToPdf.html")
    try:
        pdf = pdfkit.from_string(rendered, 'out.pdf', configuration=CONFIG)
        file = open("out.pdf","wb")
        file.write(pdf)
        file.close()
    except:
        pass
    return rendered


@app.route("/Products", methods = ['POST','GET','DELETE'])
def products():
    if request.method == 'GET':
        if session['usertype'] == None:
            return render_template('login.html', msg='Log in to use site')
        else:
            if checkAdmin():
                db = sqlite3.connect("database.db")
                curs = db.cursor()
                curs.execute("SELECT * FROM Items")
                results = curs.fetchall()

                curs.close()
                db.close()
                return render_template("products.html", data = results)
            else:
                return render_template("home.html")
    elif request.method == 'POST':
        #retrieve values
        productName = request.form.get('productName', default="Error")
        productTemp = request.form.get('productTemp', default="Error")
        countryOO = request.form.get('countryOO', default="Error")
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            #insert values into databse
            cur.execute("INSERT INTO Items ('productName', 'temperature', 'origin')\
            VALUES (?,?,?)", #this method avoids SQL injection
            (productName, productTemp, countryOO) )
            conn.commit()
            msg = "Product successfully added"
        except Exception as e:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return msg
    elif request.method == 'DELETE':
        productID= request.form.get('productID', default="Error")
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            if cur.execute("SELECT * FROM Items WHERE itemID=?;",[productID]).fetchall() == []:
                return render_template("products.html", ID="None")
            cur.execute("DELETE FROM Items WHERE itemID=?;", [productID])
            conn.commit()
            msg = "Record successfully deleted"
        except Exception as e:
            conn.rollback()
            msg = "error in delete operation"
        finally:
            conn.close()
            return msg

@app.route("/Customers")
def customer():
    if request.method == 'GET':
        if session['usertype'] == None:
            return render_template('login.html', msg='Log in to use site')
        else:
            username = request.cookies.get('username')
            if checkAdmin():
                try:
                    conn = sqlite3.connect(DATABASE)
                    cur = conn.cursor()
                    cur.execute("SELECT customerName, address, deliveryAddress FROM Customers")
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
        #retrieve values
        customerName = request.form.get('customerName', default="Error")
        address = request.form.get('address', default="Error")
        deliveryAddress = request.form.get('deliveryAddress', default="Error")
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            #insert values into database
            cur.execute("INSERT INTO Customers ('customerName', 'address', 'deliveryAddress')\
            VALUES (?,?,?)", #this method avoids SQL injection
            (customerName, address, deliveryAddress) )
            conn.commit()
            msg = "Record successfully added"
        except Exception as e:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return msg

@app.route("/Customer/UpdateCustomerName", methods = ['POST','GET'])
def update_customer():
    if request.method == 'POST':
        #retrieve values
        customerName = request.form.get('customerName', default="Error")
        newName = request.form.get('newName', default="Error")
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            #insert values into database
            cur.execute("UPDATE Customers SET customerName=? WHERE customerName=?",
            (newName, customerName,) )
            conn.commit()
            msg = "Record successfully added"
        except Exception as e:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return msg

@app.route("/Customer/UpdateCustomerAddress", methods = ['POST','GET'])
def update_customer_address():
    if request.method == 'POST':
        #retrieve values
        customerName = request.form.get('customerName', default="Error")
        newAddress = request.form.get('newAddress', default="Error")
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            #insert values into database
            cur.execute("UPDATE Customers SET address=? WHERE customerName=?",
            (newAddress, customerName,) )
            conn.commit()
            msg = "Record successfully added"
        except Exception as e:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return msg

@app.route("/Customer/UpdateCustomerDelivery", methods = ['POST','GET'])
def update_customer_delivery():
    if request.method == 'POST':
        #retrieve values
        customerName = request.form.get('customerName', default="Error")
        newDeliveryAddress = request.form.get('newDeliveryAddress', default="Error")
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            #insert values into database
            cur.execute("UPDATE Customers SET deliveryAddress=? WHERE customerName=?",
            (newDeliveryAddress, customerName,) )
            conn.commit()
            msg = "Record successfully added"
        except Exception as e:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return msg

@app.route("/Customer/DelCustomer", methods = ['DELETE','GET'])
def del_customer():
    if request.method == 'DELETE':
        name = request.form.get('name', default="Error")
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("DELETE FROM Customers WHERE customerName=?;", [name])
            conn.commit()
            msg = "Record successfully deleted"
        except Exception as e:
            conn.rollback()
            msg = "error in delete operation"
        finally:
            conn.close()
            return msg

@app.route("/Users/Add", methods=['POST','GET'])
def userAddDetails():
    if request.method == 'GET':
        return render_template("users.html")
    if request.method == 'POST':
        Firstname = request.form.get('firstname', default="Error")
        Surname = request.form.get('surname', default="Error")
        Public = request.form.get('public', default="Error")
        Username = request.form.get('username', default="Error")
        Password = request.form.get('password', default="Error")
        Password = bcrypt.hashpw(Password.encode(),b'$2b$12$5nU0TVBvc2ZD2mLE6PztrO')
        UserRole = request.form.get('role', default="False")
        try:
            db = sqlite3.connect("database.db")
            curs = db.cursor()
            curs.execute("INSERT INTO Users ('firstName', 'surname', 'public', 'username', 'password', 'role' ) VALUES (?, ?, ?, ?, ?, ?)",(Firstname, Surname, Public, Username, Password, UserRole) )
            db.commit()
            msg = "User successfully added to database"
        except Exception as e:
            db.rollback()
            msg = "Error creating user"
        finally:
            db.close()
            return msg

@app.route("/Users/UpdatePassword", methods=['POST','GET']) #has not been tested yet
def updateUserDetails():
    if request.method == 'GET':
        return render_template("users.html")
    if request.method == 'POST':
        username = request.form.get('username', default="Error")
        password = request.form.get('password', default="Error")
        try:
            db = sqlite3.connect("database.db")
            curs = db.cursor()
            curs.execute("UPDATE Users SET password=? WHERE username=?",(password, username) )
            db.commit()
            msg = "Password successfully changed"
        except Exception as e:
            db.rollback()
            msg = "Error updating user"
        finally:
            db.close()
            return msg

@app.route("/Users/UpdateRole", methods=['POST','GET']) #has not been tested yet
def updateUserRole():
    if request.method == 'GET':
        return render_template("users.html")
    if request.method == 'POST':
        username = request.form.get('username', default="Error")
        role = request.form.get('role', default="Error")
        try:
            db = sqlite3.connect("database.db")
            curs = db.cursor()
            curs.execute("UPDATE Users SET role=? WHERE username=?",(role, username) )
            db.commit()
            msg = "User successfully added to database"
        except Exception as e:
            db.rollback()
            msg = "Error updating user"
        finally:
            db.close()
            return msg

@app.route("/LogOut", methods=['GET'])
def log_out():
    if request.method == 'GET':
        username = None
        role = None
        return render_template("login.html")

if __name__ == "__main__":
	app.run(debug=True)
