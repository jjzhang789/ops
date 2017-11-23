import hashlib

def md5set(password):
    salt = "dkdf"+password+"dgfdfhuykjj"
    password = hashlib.md5(salt.encode("utf-8")).hexdigest()
    return password