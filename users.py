from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Users:
    def __init__(self):
        self.users = {}
        self.history = {}

    def add_user(self, username, email, password):
        self.users[username] = {
            'username': username,
            'email': email,
            'password': generate_password_hash(password)
        }
        self.history[username] = []

    def get_user(self, username):
        return self.users.get(username)

    def add_history(self, username, entry_type, content, result):
        entry = {
            'type': entry_type,
            'content': content,
            'result': 'fraudulent' if result else 'safe',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.history[username].append(entry)

    def get_history(self, username):
        return self.history.get(username, [])
