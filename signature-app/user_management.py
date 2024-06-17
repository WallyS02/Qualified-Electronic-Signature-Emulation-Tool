import hashlib
import os
import pandas as pd

USERS_PATH = os.path.join('data', 'users.csv')


def find_user(username):
    users = pd.read_csv(USERS_PATH)
    if users.empty:
        return 'empty'
    for index, row in users.iterrows():
        if row['username'] == username:
            return row
    return None


def get_name_and_surname(username):
    users = pd.read_csv(USERS_PATH)
    if users.empty:
        return 'empty'
    for index, row in users.iterrows():
        if row['username'] == username:
            return {'name': row['name'], 'surname': row['surname']}
    return None

def login(username, password):
    row = find_user(username)
    if row is not None and hashlib.sha256(password.encode()).hexdigest() == row['password']:
        return True
    return False


def register(username, password, name, surname):
    row = find_user(username)
    if row is not None and type(row) is not str:
        return 'Username is already taken'
    users = pd.read_csv(USERS_PATH)
    new_user = pd.DataFrame({'username': [username],
                             'password': [hashlib.sha256(password.encode()).hexdigest()],
                             'name': [name],
                             'surname': [surname]})
    users = pd.concat([users, new_user], ignore_index=True)
    users.to_csv(USERS_PATH, index=False)
    return 'User registered successfully'
