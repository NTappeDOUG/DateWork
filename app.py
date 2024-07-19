from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Home():
    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def Login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def Register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)