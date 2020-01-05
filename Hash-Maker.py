from hashing import *

if __name__ == "__main__":
        print ("""
		|------------------------------------|
		|      Hash Maker Version 4.5        |
		|<=================================>>|
		|       Welcome To Hashmaker         |
		|<=================================>>|
		|CREATOR: ORTEAM                     |
		|My Telegram Channel :T.me/fsoc_iety |
		|------------------------------------|
""")
        password = input(' Enter Your password for hashling :' )
	 
        while password =='':
            print("Set password")
            password = input(' Enter Your password for hashling :' )
		
        print ("""
		|------------------------------------|
		|      Hash Maker Version 4.5        |
		|<=================================>>|
		|---------->  OPTIONS <--------------|
		|---------->-1 MD5    <--------------|
		|---------->-2 SHA1   <--------------|
		|---------->-3 SHA224 <--------------|
		|---------->-4 SHA256 <--------------|
		|---------->-5 SHA384 <--------------|
		|---------->-6 SHA512 <--------------|
		|<=================================>>|
		|CREATOR: ORTEAM                     |
		|My Telegram Channel :T.me/fsoc_iety |
		|------------------------------------|
""")
        model = input(" select the number options : ")
        while model =='':
            print("Set OPTIONS")
            model = input(" select the number options : ")

        ig = hashing(password, model)
        ig.hashs(model, password)