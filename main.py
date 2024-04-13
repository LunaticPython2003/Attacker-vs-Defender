from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


    # if 'count' not in session:
    #     session['count'] = 0
    # if request.method == 'POST':
    #     session['count'] += 1
    #     if session['count'] > 5:
    #         return redirect('/sorry')
    #     if request.form['key'] == 'correct_key':
    #         return 'Key matched!'
    # return '''
    #     <form method="POST">
    #         <input type="text" name="key" required>
    #         <input type="submit" value="Submit">
    #     </form>
    #     <p>Attempts left: {}</p>
    # '''.format(5 - session['count'])

@app.route('/sorry')
def sorry():
    return 'Sorry, you have exceeded the maximum number of attempts.'

if __name__ == '__main__':
    app.run(debug=True)
