from flask import Flask,render_template

app = Flask(__name__)

@app.route("/", endpoint="index")
@app.route("/index")
def home_page():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/camera")
def camera():
    return render_template('camera.html')

@app.route("/gps")  # Menambahkan route untuk GPS
def gps():
    return render_template('gps.html')

@app.route("/settings")
def settings():
    return render_template('settings.html')