from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import os

app = Flask(__name__)
CORS(app)
CSV_FILE = 'submissions.csv'

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)
