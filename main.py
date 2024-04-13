from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/secret', methods=['POST'])
def secret():
    if request.method == 'POST':
        secret_key = request.form['secret']
        print(f"Received secret key: {secret_key}")
        return "GOTCHA"

@app.route('/winner', methods=['GET'])
def winner():
    return render_template("winner.html")

if __name__ == '__main__':
    app.run(debug=True)
