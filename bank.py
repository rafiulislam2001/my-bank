from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

balance = 10000.00

def check_balance():
    print(f"Your currant balance is = {balance}")

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ammount {amount} successfull.\nNew balance is = {balance}")

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient ammount, please recharge your account"
    else:
        balance -= amount
        return f"Withdrawal amount {amount} successful, new balance is = {balance}"

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/balance')
def show_balance():
    return check_balance()

@app.route('/deposit', methods=['GET', 'POST'])
def make_deposit():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        result = deposit(amount)
        return result
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def make_withdrawal():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        result = withdraw(amount)
        return result
    return render_template('withdraw.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "junaid" and password == "123wsx":
            return redirect(url_for('home'))
        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)