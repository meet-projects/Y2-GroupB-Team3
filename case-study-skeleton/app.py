from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {

  "apiKey": "AIzaSyAJ2MlenTN5PMQcFJko9FBneumi-mrurXs",
  "authDomain": "group-project-97de5.firebaseapp.com",
  "projectId": "group-project-97de5",
  "storageBucket": "group-project-97de5.appspot.com",
  "messagingSenderId": "643161578952",
  "appId": "1:643161578952:web:dcaf1c68b2bd08fc7634fd",
  "databaseURL":"https://group-project-97de5-default-rtdb.europe-west1.firebasedatabase.app/"
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db=firebase.database()



#Code goes below here
# <<<<<<< Updated upstream

@app.route('/')
def Home():
    return render_template("Home.html")



@app.route('/Join_us')
def Join_us():
    return render_template("Join_us.html")



@app.route('/partners')
def partners():
    return render_template("partners.html")



@app.route('/About_us')
def About_us():
    return render_template("About_us.html")

# =======

    
# >>>>>>> Stashed changes



#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)