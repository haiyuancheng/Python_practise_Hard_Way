#!/usr/bin/python
# -*- coding: UTF-8 -*-
#改写code

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "Three's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake"
    print "2. Scream at the bear."

    bear = raw_input("> ")
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        print "1. go with safe speed."
        print "2. go with fast speed."
        print "3. go with dangerous speed."

        speed = raw_input("> ")
        if speed == "1":
            print "The bears with a good speed."
        elif speed == "2":
            print "This is a litte fast."
        elif speed == "3":
            print "Warming dangerous!"
        else:
            print "Game over!"

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into pool of muck. Good job!"
        print "1. Apple."
        print "2. Banala."
        print "3. orange."

        kind = raw_input("> ")
        if kind >= 1 or kind <= 10:
            print "Good luck, you pick up red apples."
        else:
            print "Bad, Only left water."
else:
    print "You stumble around and fall on a knife and die. Good job!"

