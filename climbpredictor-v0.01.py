#!/usr/bin/env python
"""
climb predictor. type in something and be told where to go climbing.
@author: beefsix
@date: 2018-09-18
"""
import random
import sys
import time

def main():
    print("Climb Predictor v0.01")
    input("type 'where should I go?' or anything to predict a climb session!: ")
    rand_value = int(random.random() * 4)   #0-3 inclusive
    if rand_value == 0:
        print ("Red Rock is lookin' nice right now.")
    elif rand_value == 1:
        print("Go to Mt. Charleston and SHRED IT!")
    elif rand_value == 2:
        print ("Go to the gym - rest, recupe, and rip 'em back")
    elif rand_value == 3:
        print("Calisthenics lmao run pussy")
    print("remember to always be good to urself lad. keep it metal.")
    time.sleep(3)
    sys.exit()

if __name__ == "__main__":
    main()

# to-do

# make if statements into a list
# clean up code
# add in locale functionality
# i.e. - type "Las Vegas" or your area code and get
# a climbing location within 1 hr from you
