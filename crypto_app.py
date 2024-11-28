from flask import Flask, jsonify
import os
import requests
import logging

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi logging
logging.basicConfig(level=logging.DEBUG)

# Route untuk root URL
@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to the Crypto Price API. Visit /crypto to get prices for Bitcoin and Ethereum."
    })

# Route untuk mendapatkan harga crypto
@app.route("/crypto", methods=["GET"])
def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd"
    }
    try:
        # Mengirim permintaan ke CoinGecko menggunakan proxy
        response = requests.get(url, params=params, proxies=proxies)
        response.raise_for_status()  # Cek jika ada error
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        # Menangkap error dan mencatatnya
        logging.error(f"Error fetching data: {e}")
        return jsonify({"error": str(e)}), 500

# Menjalankan aplikasi jika file ini dieksekusi langsung
#if __name__ == "__main__":
#    port = int(os.environ.get("PORT", 8080))  # Menggunakan port dari environment Railway
#    app.run(debug=True, host="0.0.0.0", port=port)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
