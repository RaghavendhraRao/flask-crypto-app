from flask import Flask, render_template
import requests

app = Flask(__name__)

# @app.route('/')
# def index():
#     response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
#     data = response.json()
#     price = data['bpi']['USD']['rate']
#     return render_template('index.html', price=price)


print("This is the testing app..!")
print("This Page will show the BTC price...!")

@app.route('/')
def index():
    # MOCK data instead of calling external API
    price = "42,000.99"  # fake BTC price for testing
    return render_template('index.html', price=price)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
