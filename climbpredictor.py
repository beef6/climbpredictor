#!/usr/bin/env python3
"""
climb predictor. type in something and be told where to go climbing.
@author: beefsix
@date: 2018-09-18
"""
import sys
import random
import time

def main():
    climbing_places = ["Red Rock is lookin' nice tbh.", "Go to Mt. Charleston and SHRED IT!",
                       "Go to the gym - rest, recupe, and rip 'em back my guy.", "Calisthenics lmao run pussy"
                      ]    # PEPS compliance
    print("Climb Predictor v0.02")
    input("type 'where should I go?' or anything to predict a climb session!: ")
    print(random.choice(climbing_places))
    go_again = input("Is that a good spot right now? (y/n): ")
    if go_again[0].lower() == "n":
        sys.exit(0)
    print("remember to always be good to urself lad. keep it metal.\n666")

if __name__ == "__main__":
    main()

# to-do

## add in locale functionality
# i.e. - type "Las Vegas" or your area code and get
# a climbing location within 1 hr from you
