import hashlib
import random
from time import sleep
class hashing:

    def __init__(self, password, model):
        self.password = password
        self.model = model
		
    def hashs(self, model, password):

        if model == "1":
            md5 = hashlib.md5(password.encode())
            print("""
	|------------------------------------|
	|       Md5 Your Password is         |
	|<=================================>>|
	|""",md5.hexdigest(),"""  |
	|<=================================>>|
	|CREATOR: ORTEAM                     |
	|My Telegram Channel  T.me/fsoc_iety |
	|------------------------------------|
""")
        elif model == "2":
            sha1 = hashlib.sha1(password.encode())
            print("""
	|------------------------------------------|
	|          Sha1 Your Password is           |
	|<=======================================>>|
	|""",sha1.hexdigest(),"""|
	|<=======================================>>|
	|CREATOR: ORTEAM                           |
	|My Telegram Channel  T.me/fsoc_iety       |
	|------------------------------------------|
""")
        elif model == "3":
            sha224 = hashlib.sha224(password.encode())
            print("""
	|----------------------------------------------------------|
	|                Sha224 Your Password is                   |
	|<=======================================================>>|
	|""",sha224.hexdigest(),"""|
	|<=======================================================>>|
	|CREATOR: ORTEAM                                           |
	|My Telegram Channel  T.me/fsoc_iety                       |
	|----------------------------------------------------------|
""")
        elif model == "4":
            sha256 = hashlib.sha256(password.encode())
            print("""
	|------------------------------------------------------------------|
	|                    Sha256 Your Password is                       |
	|<===============================================================>>|
	|""",sha256.hexdigest(),"""|
	|<===============================================================>>|
	|CREATOR: ORTEAM                                                   |
	|My Telegram Channel  T.me/fsoc_iety                               |
	|------------------------------------------------------------------|
""")
        elif model == "5":
            sha384 = hashlib.sha384(password.encode())
            print("""
	|--------------------------------------------------------------------------------------------------|
	|                                  Sha384 Your Password is                                         |
	|<===============================================================================================>>|
	|""",sha384.hexdigest(),"""|
	|<===============================================================================================>>|
	|CREATOR: ORTEAM                                                                                   |
	|My Telegram Channel  T.me/fsoc_iety                                                               |
	|--------------------------------------------------------------------------------------------------|
""")
        elif model == "6":
            sha512 = hashlib.sha512(password.encode())
            print("""
	|----------------------------------------------------------------------------------------------------------------------------------|
	|                                               Sha512 Your Password is                                                            |
	|<===============================================================================================================================>>|
	|""",sha512.hexdigest(),"""|
	|<===============================================================================================================================>>|
	|CREATOR: ORTEAM                                                                                                                   |
	|My Telegram Channel  T.me/fsoc_iety                                                                                               |
	|----------------------------------------------------------------------------------------------------------------------------------|
""")
class psgn:
    def psswod():
        sm = "abcdefghijklmnopqrstuvwxyz"
        bi = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = "0123456789"
        sl = "[]{}()*@#;:,_-$%&^!><./"
        
        alls = sm + bi + num + sl
        l = 16
        passwd = "".join(random.sample(alls, l))
        print(">>> Please Wait Create Your Password")
        sleep(1)
        print("""
	 >>> """,passwd,"""
        <<=======================================>>
	 >>> CREATOR: ORTEAM
	 >>> My Telegram Channel  T.me/fsoc_iety
""")
