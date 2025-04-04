from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/crash', methods=['GET'])
def crash():
    crash_point = round(random.uniform(1.00, 10.00), 2)
    return jsonify({'crash_point': crash_point})

@app.route('/bet', methods=['POST'])
def bet():
    data = request.json
    bet_amount = data.get('amount')
    return jsonify({'status': 'bet_placed', 'amount': bet_amount})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
