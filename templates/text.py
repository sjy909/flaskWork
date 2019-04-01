# import hashlib
# print(hashlib)

from hashlib import md5
s1 = "123".encode("utf8")
md5 = md5()

pad = md5.hexdigest()

print(pad)
