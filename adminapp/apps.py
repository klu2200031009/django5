from django.apps import AppConfig


class AdminappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adminapp'
import stripe
from flask import Flask, request, jsonify, render_template

# Set up your Flask application
app = Flask(__name__)

# Stripe API key setup
stripe.api_key = 'your-secret-key'  # Replace 'your-secret-key' with your actual Stripe secret key

# Route to display the payment form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the payment
@app.route('/pay', methods=['POST'])
def pay():
    # Amount in cents (e.g., 500 cents = $5.00)
    amount = 500

    # Create a charge: this will charge the user's card
    try:
        # Token is created using Stripe's JavaScript library to tokenize credit card details
        token = request.form['stripeToken']  # Assuming your payment form sends a token to this route

        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='Example charge',
            source=token,
        )

        return jsonify(charge), 200

    except stripe.error.StripeError as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
