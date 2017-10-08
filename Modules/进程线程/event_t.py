#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 通过Event可以实现两个或多个线程间的交互
# An event is a simple synchronization object；the event represents an internal flag
# event = threading.Event()=====实例化一个event
# event.set()=================== set the flag
# event.clear()================= clear the flag
# event.isSet()================= judge flag is set or not
# event.wait()==================If the flag is set, the wait method doesn’t do anything;If the flag is cleared, wait will block[阻塞] until it becomes set again


import threading,time
import random
def light():
    if not event.isSet():
        event.set() #wait就不阻塞 #绿灯状态
    count = 0
    while True:
        if count < 10:
            print('\033[42;1m--green light on---\033[0m')
        elif count <13:
            print('\033[43;1m--yellow light on---\033[0m')
        elif count <20:
            if event.isSet():
                event.clear()
            print('\033[41;1m--red light on---\033[0m')
        else:
            count = 0
            event.set() #打开绿灯
        time.sleep(1)
        count +=1
def car(n):
    while 1:
        time.sleep(random.randrange(10))
        if  event.isSet(): #绿灯
            print("car [%s] is running.." % n)
        else:
            print("car [%s] is waiting for the red light.." %n)
if __name__ == '__main__':
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(3):
        t = threading.Thread(target=car,args=(i,))
        t.start()