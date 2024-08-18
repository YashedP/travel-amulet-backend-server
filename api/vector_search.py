from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/vector_search', methods=['GET'])
def vector_search():
    # Get the 'text' parameter from the request
    text = request.args.get('prompt')

    # Check if the 'text' parameter is provided
    if text:
        return jsonify({"message": f"You sent the string: {text}"})
    else:
        return jsonify({"error": "No string provided"}), 400