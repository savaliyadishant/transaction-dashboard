from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Define the correct password
CORRECT_PASSWORD = 'mypassword'  # Change this to your desired password

# Connect to your cloud MongoDB database
try:
    client = MongoClient("mongodb+srv://savaliyadishant3:zWYsuhySLltfii5v@cluster0.grxeu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Replace with your MongoDB URI
    db = client['Transactions']
    collection = db['transactions']
    # Test the connection
    collection.find_one()
    print("Database connection successful.")
except Exception as e:
    print("Database connection failed:", e)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        entered_password = request.form['password']
        if entered_password == CORRECT_PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            error = 'Incorrect password. Please try again.'
            return render_template('index.html', error=error)
    return render_template('index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    friend_name = None
    transactions = []
    message = ""
    message_type = ""
    balance_message = ""

    if request.method == 'POST':
        # Handle adding a new transaction
        if 'name' in request.form:
            try:
                transaction = {
                    'name': request.form['name'],
                    'amount': float(request.form['amount']),
                    'transaction_type': request.form['transaction_type'],
                    'payment_method': request.form['payment_method'],
                    'date': request.form['date']
                }
                collection.insert_one(transaction)
                message = "Transaction added successfully!"
                message_type = "success"
            except Exception as e:
                message = f"Error adding transaction: {e}"
                message_type = "error"
            return render_template('dashboard.html', message=message, message_type=message_type)

        # Handle searching for transactions
        friend_name = request.form['friend_name']
        if friend_name:
            # Fetch the last five transactions for the given friend name, sorted by date in descending order
            transactions = list(collection.find({'name': friend_name}).sort('date', -1).limit(5))

            # MongoDB Aggregation Pipeline to calculate the balance
            pipeline = [
                {'$match': {'name': friend_name}},
                {'$group': {
                    '_id': '$transaction_type',
                    'total': {'$sum': '$amount'}
                }}
            ]

            # Execute the aggregation pipeline
            result = list(collection.aggregate(pipeline))

            total_credit = 0
            total_debit = 0

            for record in result:
                if record['_id'] == 'Credit':
                    total_credit = record['total']
                elif record['_id'] == 'Debit':
                    total_debit = record['total']

            # Determine the balance message
            if total_credit > total_debit:
                balance_message = f"{friend_name} owes you {total_credit - total_debit}."
            elif total_debit > total_credit:
                balance_message = f"You owe {friend_name} {total_debit - total_credit}."
            else:
                balance_message = "No outstanding balance with this friend."

    return render_template('dashboard.html', friend_name=friend_name, transactions=transactions, message=message, message_type=message_type, balance_message=balance_message)

if __name__ == "__main__":
    app.run(debug=True)