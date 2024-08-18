from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/check_string', methods=['GET'])
def check_string():
    # Get the 'text' parameter from the request
    text = request.args.get('text')

    # Check if the 'text' parameter is provided
    if text:
        return jsonify({"message": f"You sent the string: {text}"})
    else:
        return jsonify({"error": "No string provided"}), 400