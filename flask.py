from flask import Flask, jsonify
import requests
import logging

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi logging
logging.basicConfig(level=logging.DEBUG)

# Definisikan route untuk mendapatkan harga crypto
@app.route("/crypto", methods=["GET"])
def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd"
    }
    try:
        # Mengirim permintaan ke CoinGecko
        response = requests.get(url, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        # Menangkap error dan mencatatnya
        logging.error(f"Error fetching data: {e}")
        return jsonify({"error": str(e)}), 500

# Menjalankan aplikasi jika file ini dieksekusi langsung
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
