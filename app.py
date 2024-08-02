from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({"is_success": False}), 400

        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_alphabet = max(alphabets, key=str.lower) if alphabets else None

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with your actual details
            "email": "john@xyz.com",    # Replace with your actual email
            "roll_number": "ABCD123",    # Replace with your actual roll number
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
