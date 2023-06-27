from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/admissionreference')
def adref():
    return render_template('adrefscreen.html')

@app.route("/register", methods=["GET"])
def register():
    return redirect("http://127.0.0.1:5000/admissionreference", code=302)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
