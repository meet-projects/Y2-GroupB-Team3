from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {
  apiKey: "AIzaSyBylDOMbYa1vsU-BxgstPmfl9hTYn5XbQQ",
  authDomain: "final-project-9552e.firebaseapp.com",
  databaseURL: "https://final-project-9552e-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "final-project-9552e",
  storageBucket: "final-project-9552e.appspot.com",
  messagingSenderId: "848642725083",
  appId: "1:848642725083:web:b0b26fb00e4bf03dff28fe",
  measurementId: "G-7SJLWPFJM6"
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here
# <<<<<<< Updated upstream

@app.route('/')
def index():
    return render_template("index.html")

# =======
@app.route('/')
def home():
    
>>>>>>> Stashed changes



#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)