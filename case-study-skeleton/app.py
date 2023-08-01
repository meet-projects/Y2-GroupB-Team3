from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyBkCc1WY7Yu2BETjmYA6m3jmHYU4Ll5qMI",
  "authDomain": "fir-17f02.firebaseapp.com",
  "databaseURL": "https://fir-17f02-default-rtdb.firebaseio.com",
  "projectId": "fir-17f02",
  "storageBucket": "fir-17f02.appspot.com",
  "messagingSenderId": "787139879406",
  "appId": "1:787139879406:web:e62a546ade52375942eeff",
  "measurementId": "G-K9LW85TTZH",
  "databaseURL":"https://fir-17f02-default-rtdb.firebaseio.com/"
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db=firebase.database()


@app.route('/')
def Home():
    return render_template("Home.html")



@app.route('/Join_us', methods = ['GET','POST'])
def Join_us():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        companys_name = request.form['companys_name']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, username)
            UID = login_session['user']['localId']
            user = {"email":email, 'companys_name':companys_name}
            db.child("Users").child(UID).set(user)
            return redirect(url_for('thanku'))
        except:
            error = "Authentication failed"
            print(error)
    return render_template("Join_us.html")


@app.route('/apply', methods = ['GET','POST'])
def apply():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        fullname = request.form['fullname']
        age = request.form['age']
        profession = request.form['profession']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, username)
            UID = login_session['user']['localId']
            user = {"email":email, 'fullname':fullname, 'age': age, "profession":profession}
            db.child("Users").child(UID).set(user)
            return redirect(url_for('thanku'))
        except:
            error = "Authentication failed"
            print(error)
    return render_template("apply.html")




@app.route('/partners')
def partners():
    return render_template("partners.html")



@app.route('/About_us')
def About_us():
    return render_template("About_us.html")


@app.route('/talents')
def talents():
    return render_template("talents.html")



@app.route('/alumni')
def alumni():
    return render_template("alumni.html")



@app.route('/companies')
def companies():
    return render_template("companies.html")


@app.route('/thanku')
def thanku():
    return render_template("thanku.html")

#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)