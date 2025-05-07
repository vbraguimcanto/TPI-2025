from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    if response.status_code == 200:
        return jsonify(response.json()), 200
    return jsonify({'error': 'Failed to fetch data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
