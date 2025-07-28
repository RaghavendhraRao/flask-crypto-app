from flask import Flask, render_template
import requests
import logging


# Logging setup
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
)


app = Flask(__name__)

# @app.route('/')
# def index():
#     response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
#     data = response.json()
#     price = data['bpi']['USD']['rate']
#     return render_template('index.html', price=price)



@app.route('/')
def index():
    try:
        # MOCK data instead of calling external API
        price = "42,000.998"  # fake BTC price for testing
        logging.info("Fetched Bitcoin rate successfully.")
        return render_template('index.html', price=price)
    except Exception as e:
        logging.error(f"Error fetching Bitcoin rate: {e}")
        return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
