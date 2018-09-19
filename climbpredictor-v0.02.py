#!/usr/bin/env python3
"""
climb predictor. type in something and be told where to go climbing.
@author: beefsix
@date: 2018-09-18
"""
import sys 
import random
import time

climbing_places = ["Red Rock is lookin' nice right now", "Go to Mt. Charleston and SHRED IT!", "Go to the gym - rest, recupe, and rip 'em back", "Calisthenics lmao run pussy"]

def main():
    print("Climb Predictor v0.02")
    input("type 'where should I go?' or anything to predict a climb session!: ")
    print(random.choice(climbing_places)) 
    
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
