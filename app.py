from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Backend!"

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!", "data": [1, 2, 3, 4, 5]})

if __name__ == '__main__':
    app.run(debug=True)
