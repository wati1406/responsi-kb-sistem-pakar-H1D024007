from flask import Flask, render_template, request, jsonify
from pakar_boros import diagnosa_boros

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pakar.html')

@app.route('/api/pakar', methods=['POST'])
def api_pakar():
    data = request.json
    hasil = diagnosa_boros(jawaban=data['jawaban'])
    return jsonify(hasil)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # beda port biar tidak bentrok