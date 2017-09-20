#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

menu = {
    '北京':{
        "昌平":{
            "沙河":{"oldboy","test"},
            "天通苑":{"链家地产","我爱我家"}
        },
        "朝阳":{
            "望京":{"奔驰","陌陌"},
            "国贸":{'CICC',"HP"},
            "东直门":{"Advent","飞信"}
        },
        "海淀":{}
    },
    '山东':{
        "德洲":{},
        "青岛":{},
        "济南":""
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{}
    }
}
exit_flag = False

while not exit_flag:
    for i in menu:
        print(i)
    choice = input("plz choose[q for quit]>>:")
    if choice == "q":
        exit_flag = True
        #break
    elif choice in menu:
        while not exit_flag:
            for j in menu[choice]:
                print("\t", j)
            choice1 = input("plz choose[b for back|q for quit]>>:")
            if choice1 == "b":
                break
            elif choice1 == "q":
                exit_flag = True
                #break
            elif choice1 in menu[choice]:
                while not exit_flag:
                    for z in menu[choice][choice1]:
                        print("\t\t", z)
                    choice2 = input("plz choose[b for back|q for quit]>>:")
                    if choice2 == "b":
                        break
                    elif choice2 == "q":
                        exit_flag = True
                        #break
                    elif choice2 in menu[choice][choice1]:
                        print(menu[choice][choice1][choice2])
                    else:
                        print("\033[31;1mError Choice;plz choose again\033[0m")
            else:
                print("\033[31;1mError Choice;plz choose again\033[0m")
    else:
        print("\033[31;1mError Choice;plz choose again\033[0m")


