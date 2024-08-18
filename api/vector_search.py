from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/vector_search', methods=['GET'])
def vector_search():
    # Get the 'text' parameter from the request
    text = request.args.get('prompt')

    # Check if the 'text' parameter is provided
    if text:
        return jsonify({"message": f"You sent the string: {text}"})
    else:
        return jsonify({"error": "No string provided"}), 400