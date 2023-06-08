from werkzeug.security import check_password_hash


def check_password(hashed_password, password):
    return check_password_hash(hashed_password, password)


check_password('1234', password)