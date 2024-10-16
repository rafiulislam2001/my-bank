from flask import Flask, render_template, request, redirect, url_for, session
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

app.secret_key = 'supersecretkey'

balance = 10000.00

def check_balance():
    return f"Your current balance is = {balance:.2f}"

def deposit(amount):
    global balance
    balance += amount
    return f"Deposited amount {amount} successfully.\nNew balance is = {balance:.2f}"

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient balance, please recharge your account"
    else:
        balance -= amount
        return f"Withdrawal of {amount} successful, new balance is = {balance:.2f}"

# Define routes
@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/balance')
def show_balance():
    result = check_balance()
    return f"<h3>{result}</h3>"

@app.route('/deposit', methods=['GET', 'POST'])
def make_deposit():
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            result = deposit(amount)
            return f"<h3>{result}</h3>"
        except ValueError:
            return "Invalid input, please enter a numeric value."
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def make_withdrawal():
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            result = withdraw(amount)
            return f"<h3>{result}</h3>"
        except ValueError:
            return "Invalid input, please enter a numeric value."
    return render_template('withdraw.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Simple username/password check
        if username == "junaid" and password == "123wsx":
            session['username'] = username  # Mark user as logged in
            return redirect(url_for('home'))  # Redirect to home page after login
        else:
            return "Invalid credentials. Please try again."
    
    # Render login page for GET request
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)