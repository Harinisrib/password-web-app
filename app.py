from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Character sets
letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!#$%&()*+')

# Password generator function
def generate_password(no_letters, no_symbols, no_numbers):
    password = ""
    for _ in range(no_letters):
        password += random.choice(letters)
    for _ in range(no_symbols):
        password += random.choice(symbols)
    for _ in range(no_numbers):
        password += random.choice(numbers)
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        try:
            no_letters = int(request.form['letters'])
            no_symbols = int(request.form['symbols'])
            no_numbers = int(request.form['numbers'])
            password = generate_password(no_letters, no_symbols, no_numbers)
        except:
            password = "Please enter valid numbers!"
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
