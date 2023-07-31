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
        fullname = request.form['fullname']
        username = request.form['username']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, username)
            UID = login_session['user']['localId']
            user = {"fullname":fullname,"username": username,"email":email}
            db.child("Users").child(UID).set(user)
            return redirect(url_for('About_us'))
        except:
            error = "Authentication failed"
            print(error)
    return render_template("Join_us.html")



@app.route('/partners')
def partners():
    return render_template("partners.html")



@app.route('/About_us')
def About_us():
    return render_template("About_us.html")

#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)