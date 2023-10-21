# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below
@app.route('/login', methods = ['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']
    if username=='verify' and password=='12345':
        account_sid = "AC81f77b807731ea5f4436b52cb0c6ff6f"
        auth_token = "200b6b82c4109de166b2c00cbded553e"
        client(account_sid, auth_token)
        verification = client.verify \
            .services('VA7fc78048d1f778525a25e5513a8fd807') \
            .verifications \
            .create(to= mobile_number, channel='sms')
        print(verification.status)
        return render_template(otp_verify.html)
    else:
        return "Entered User ID or password is wrong"
if __name__ == "__main__":
    app.run()

