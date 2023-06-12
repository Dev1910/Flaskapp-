from flask import Flask, jsonify

app = Flask(__name__)

# Define a route for the API endpoint
@app.route('/api/hello', methods=['GET'])
def api_hello():
    data = {
        'message': 'Hello, API!'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
