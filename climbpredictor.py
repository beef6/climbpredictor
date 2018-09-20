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
    climbing_places = {"702" : ["Red Rock is lookin' nice tbh.", "Go to Mt. Charleston and SHRED IT!", "Go to the gym - rest, recupe, and rip 'em back my guy.", "Calisthenics lmao run pussy"], "89124" : ["Robber's Roost", "Roadkill Traverse", "Starter Crag", "The Subway"], "LA" : ["Stony Point Park", "La Brea Tar Pits", "Skid Row"]}
    print("Climb Predictor v0.02")
    location = climbing_places[input("Enter the area code you plan to climb in: ")]
    print(random.choice(location))
    go_again = input("Is that a good spot right now? (y/n): ")
    if go_again[0].lower() == "n":
        print("well fuck dude sorry mb")
        sys.exit(0)
    print("remember to always be good to urself lad. keep it metal.\n666")

if __name__ == "__main__":
    main()

# to-do

# Improve locale functionality - clean up code, delete giant block of list text
#
# Add in prompts for asking what kind of climbing you're able to do right now
#   * bouldering, sport, trad
#   * if gym, shoot for style and grade/exercises
