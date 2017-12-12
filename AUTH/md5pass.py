import hashlib

#对密码进行加密处理
def md5set(password):
    salt = "dkdf"+password+"dgfdfhuykjj"
    password = hashlib.md5(salt.encode("utf-8")).hexdigest()
    return password