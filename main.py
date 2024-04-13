from flask import Flask, render_template, request, redirect, url_for
import base64

app = Flask(__name__)
app.data = ""
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/secret', methods=['POST'])
def secret():
    if request.method == 'POST':
        decoded_data = base64.b64decode(app.data)
        print(decoded_data)
        secret_key = request.form['secret']
        print(f"Received secret key: {secret_key}")
        if decoded_data.decode('utf-8') == secret_key:
            return render_template("winner.html")
        else:
            return "Hello"

if __name__ == '__main__':
    with open('static/secret.txt') as file:
        app.data = file.read()
    app.run(debug=True)
