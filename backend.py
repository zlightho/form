from flask import Flask, request, jsonify, send_from_directory, send_file
import csv
import os

app = Flask(__name__, static_folder="", static_url_path="")
CSV_FILE = 'submissions.csv'

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    # Для отдачи статики (css, js, иконки и т.д.)
    return send_from_directory('.', path)

@app.route('/download', methods=['GET'])
def download_csv():
    return send_file(CSV_FILE, as_attachment=True)

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
