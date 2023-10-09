from hashing import *
import sys
from time import sleep
print("""
     |    (@@@@@@@@@)    (@@@@@@@@)  (@@@@@@@@@@)  (@@@@@@@)    (@@@@@)     (@@@@@   @@@@@) | 
     |  (@@@@    @@@@)  (@@@   @@@)     (@@@)     (@@@)        (@@@ @@@)    (@@@@@  @@@@@@) |
     | (@@@@     @@@@)  (@@@@@@)       (@@@)     (@@@@@@@@)  (@@@@  @@@)   (@@@  @@@@  @@)  |
     |  (@@@    @@@@)  (@@@  @@@@)     (@@@)     (@@@)      (@@@@@@@@@@)   (@@@       @@@)  |
     |   (@@@@@@@@)    (@@@   @@@)    (@@@)     (@@@@@@@@) (@@@      @@@) (@@@       @@@)   |
     |                                                                                      |
     |_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-| 
""")
def maker():
        if __name__ == "__main__":
                print ("""
		|------------------------------------|
		|      Hash Maker Version 5.0        |
		|<=================================>>|
		|---------->  OPTIONS <--------------|
		|---------->-1 MD5    <--------------|
		|---------->-2 SHA1   <--------------|
		|---------->-3 SHA224 <--------------|
		|---------->-4 SHA256 <--------------|
		|---------->-5 SHA384 <--------------|
		|---------->-6 SHA512 <--------------|
		|>>>>>>>-7 password generator <<<<<<<|
		|>>>>>>>>>>>> Ctrl + C <<<<<<<<<<<<<<|
		|<=================================>>|
		|CREATOR: ORTEAM                     |
		|My Telegram Channel :T.me/fsoc_iety |
		|------------------------------------|
""")
                model = input(">>> select the number options : ")
                while model =='':
                    print(">>> Set OPTIONS")
                    model = input(">>> select the number options : ")
            
                if model == "7":
                        psgn.psswod()
                else:
                
                        password = input('>>> Enter Your password for hashling :' )
	 
                        while password =='':
                                print(">>> Set password")
                                password = input('>>> Enter Your password for hashling :' )


                        ig = hashing(password, model)
                        ig.hashs(model, password)
while True:
        try:
                sleep(1)
                maker()
        except KeyboardInterrupt:
                print("\n >>> Exit Hash Maker....")
                sys.exit()
