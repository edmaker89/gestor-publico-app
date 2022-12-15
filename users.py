from connection import Database

class User(Database):

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    



    def __repr__(self): 
        return f"{self.id}: {self.username}"




users = [User(1, "bob", "asdf"), User(2, "joe", "asdf"), User(3, "jane", "asdf")]
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)