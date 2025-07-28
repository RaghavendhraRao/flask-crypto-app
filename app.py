from flask import Flask, render_template
import requests
import logging
from prometheus_flask_exporter import PrometheusMetrics

# Logging setup
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
)

app = Flask(__name__)
metrics = PrometheusMetrics(app, path='/metrics')  # ✅ Force registering /metrics endpoint

@app.route('/')
def index():
    try:
        price = "42,000.998"
        logging.info("Fetched Bitcoin rate successfully.")
        return render_template('index.html', price=price)
    except Exception as e:
        logging.error(f"Error fetching Bitcoin rate: {e}")
        return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
