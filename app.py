from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)


# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  message TEXT NOT NULL,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()


# API endpoint to handle form submission
@app.route('/api/contact', methods=['POST'])
def submit_contact():
    try:
        # Get JSON data from the request
        data = request.get_json()

        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        # Validate input
        if not all([name, email, message]):
            return jsonify({'error': 'All fields are required'}), 400

        # Insert into database
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)',
                  (name, email, message))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Message sent successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Optional: Endpoint to get all contacts (for admin purposes)
@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    try:
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('SELECT * FROM contacts ORDER BY timestamp DESC')
        contacts = c.fetchall()
        conn.close()

        # Convert to list of dictionaries
        contacts_list = [
            {
                'id': contact[0],
                'name': contact[1],
                'email': contact[2],
                'message': contact[3],
                'timestamp': contact[4]
            } for contact in contacts
        ]

        return jsonify(contacts_list), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Initialize database when app starts
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)