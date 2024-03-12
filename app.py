# myenv\Scripts\activate
#docker build -t jobboard:1.0 .
#docker run -p 5000:5000 jobboard:1.0
#docker rmi jobboard:1.0 --force
#IBM DATA SERVER DRIVER
from flask import Flask, render_template, request, session
import ibm_db
# os.add_dll_directory(r"C:\Users\Ayush\OneDrive\Desktop\portfolio\CAD")
# import ibm_db
#os.add_dll_directory('C:\\Users\\Ayush\\Program Files\\IBM\\CLIDRIVER\\bin')
# import sys
# import os
# os.add_dll_directory('C:\\Program Files\\IBM\\DSDRIVER\\bin')


app=Flask(__name__)

conn = ibm_db.connect("database=bludb;hostname=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;port=32731;uid=kdm09669;pwd=UU9P108YfK2W21g7;security=SSL;sslcertificate=DigiCertGlobalRootCA.crt"," "," ")
print(conn)

connState=ibm_db.active(conn)
print(connState)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #here you can give any random bytes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jobsbrowse")
def jobbrowse():
    return render_template("job-list.html")

@app.route("/jobpost")
def jobpost():
    return render_template("job-post.html")

@app.route("/jobview")
def jobview():
    return render_template("job-view.html")

@app.route("/login",methods=['GET','POST'])
def login():
    global uemail
    if request.method == "POST":
        email=request.form['email']
        password=request.form['password']
        details=[email,password]
        print(details)
        sql="SELECT * FROM REGISTER_CAD where EMAILID=? AND PASSWORD=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        acc=ibm_db.fetch_assoc(stmt)
        print(acc)
        if acc:
            session['email']=email
            session['username']=acc['NAME']
            uemail=session['email']
            return render_template("profile.html",username=session['username'],email=session['email'])
        else:
            msg="Invalid Credintials !! Try again..."
            return render_template("login.html",message=msg)

    return render_template("login.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == "POST":
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        role=request.form['role']
        details=[name,email,password,role]
        print(details)
        sql="SELECT * FROM REGISTER_CAD where EMAILID=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        acc=ibm_db.fetch_assoc(stmt)
        print(acc)
        if acc:
            msg="You have been already Registered !! Login here ...."
            return render_template("login.html", message=msg)
        else :
            sql="INSERT into REGISTER_CAD values (?,?,?,?)"
            stmt=ibm_db.prepare(conn,sql)
            ibm_db.bind_param(stmt,1,name)
            ibm_db.bind_param(stmt,2,email)
            ibm_db.bind_param(stmt,3,password)
            ibm_db.bind_param(stmt,4,role)
            ibm_db.execute(stmt)
            msg="You have successfully registered, Please login..."
            return render_template("login.html",message=msg)
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("email",None)
    session.pop("username",None)
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)