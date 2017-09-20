
#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

import getpass
_username = "anony"
_password = "12345"
#UserCount = 0
#PawdCount = 0
#while UserCount < 3:
for i in range(3):
    username = input("username:")
    if _username == username:
        #while PawdCount < 3:
        for j in range(3):
            password = getpass.getpass("password:")
            if _password == password:
                print("welcome user {name} login...".format(name=username))
                break
            else:
                print("Error password;Plz enter again")
            #PawdCount += 1
        else:
            print("sorry")
            break
        break
    else:
        print("Invalid username;Plz enter again")
    #UserCount += 1
else:
    print("you have tried too many times....fuck off")



