from flask import Flask, request, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain(difficulty=4)

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append({
            'index': block.index,
            'timestamp': block.timestamp,
            'data': block.data,
            'previous_hash': block.previous_hash,
            'nonce': block.nonce,
            'hash': block.hash
        })
    return jsonify({
        'length': len(chain_data),
        'chain': chain_data
    }), 200

@app.route('/mine', methods=['POST'])
def mine_block():
    data = request.get_json()
    if not data or 'data' not in data:
        return jsonify({'message': 'Missing data'}), 400

    block = blockchain.add_block(data['data'])

    response = {
        'message': 'Block mined successfully!',
        'index': block.index,
        'timestamp': block.timestamp,
        'data': block.data,
        'previous_hash': block.previous_hash,
        'nonce': block.nonce,
        'hash': block.hash
    }
    return jsonify(response), 201

@app.route('/validate', methods=['GET'])
def validate_chain():
    is_valid = blockchain.is_chain_valid()
    return jsonify({'valid': is_valid}), 200

if __name__ == '__main__':
    app.run(debug=True)
