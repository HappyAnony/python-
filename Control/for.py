#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

import getpass
_username = "anony"
_password = "12345"
for i in range(3):
    username = input("username:")
    if _username == username:
        for j in range(3):
            password = getpass.getpass("password:")
            if _password == password:
                print("welcome user {name} login...".format(name=username))
                break
            else:
                print("Error password;Plz enter again")
        else:
            print("sorry")
            break
        break
    else:
        print("Invalid username;Plz enter again")
else:
    print("you have tried too many times....fuck off")